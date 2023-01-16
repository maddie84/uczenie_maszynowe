import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def getHandMove(hand_landmarks):
    landmarks = hand_landmarks.landmark
    if (landmarks[5].y < landmarks[8].y) and (landmarks[9].y < landmarks[12].y) and (
            landmarks[13].y < landmarks[16].y) and (landmarks[17].y < landmarks[20].y):
        return "rock"
    elif (landmarks[13].y < landmarks[16].y) and (landmarks[17].y < landmarks[20].y):
        return "scissors"
    else:
        return "paper"


video = cv2.VideoCapture(0)

clock = 0
p1_move = p2_move = None
gameText = ""
winner = ""
sucess = True
hands = mp_hands.Hands()

while True:
    success, img = video.read()
    if not success or img is None: break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img,
                                      handLms,
                                      mp_hands.HAND_CONNECTIONS,
                                      mp_drawing_styles.get_default_hand_landmarks_style(),
                                      mp_drawing_styles.get_default_hand_connections_style())

    img = cv2.flip(img, 1)
    img = cv2.resize(img, (1024, 768))

    if 0 <= clock <= 20:
        sucess = True
        gameText = "Ready?"
        winner = ""
    elif clock < 30:
        gameText = "3..."
        winner = ""
    elif clock < 40:
        gameText = "2..."
        winner = ""
    elif clock < 50:
        gameText = "1..."
        winner = ""
    elif clock < 60:
        gameText = "GO!"
        winner = ""
    elif clock == 60:
        hls = results.multi_hand_landmarks
        if hls and len(hls) == 2:
            p1_move = getHandMove(hls[0])
            p2_move = getHandMove(hls[1])
        else:
            sucess = False
            print(sucess)
    elif clock < 120:
        if sucess:
            gameText = f"Player 1 played {p1_move}. Player 2 played {p2_move}."
            winner = ""
            if p1_move == "scissors" and p2_move == "paper":
                winner = "Player 1 wins!"
            elif p1_move == "paper" and p2_move == "rock":
                winner = "Player 1 wins!"
            elif p1_move == "rock" and p2_move == "scissors":
                winner = "Player 1 wins!"
            elif p1_move == p2_move:
                winner = "It's a tie!"
            else:
                winner = "Player 2 wins!"
        else:
            gameText = f"Played incorrectly"
            winner = ""

    cv2.putText(img, f"Clock: {clock}", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (144, 255, 137), 2, cv2.LINE_AA)
    cv2.putText(img, gameText, (10, 80), cv2.FONT_HERSHEY_PLAIN, 2, (106, 246, 253), 2, cv2.LINE_AA)
    cv2.putText(img, winner, (10, 120), cv2.FONT_HERSHEY_PLAIN, 2, (255, 169, 244), 2, cv2.LINE_AA)
    clock = (clock + 1) % 120

    cv2.imshow("Image", img)
    cv2.waitKey(1)

video.release()
# cv2.destroyAllWindows()
#
