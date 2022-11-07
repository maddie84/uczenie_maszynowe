import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# ctr + ? - komentarz

def pictures(path):
    img = cv2.imread(path)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a = pytesseract.image_to_string(img_convert)
    print(a)

pictures('biedronka.png')
pictures('google.png')
pictures('amazon.png')
pictures('sony.png')
pictures('ck.png')
