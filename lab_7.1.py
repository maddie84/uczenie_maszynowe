import cv2

img = cv2.imread('plaza.jpg') #otwiera obraz

cv2.imshow('image', img)
cv2.waitKey(0) #wyswietla dopoki czegos nie nacisne
cv2.destroyAllWindows() #zamyka sie po nacisnieciu

print(type(img)) #
print(img.shape) #wymiar obrazka

img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #konwertowanie na czrano-biale

cv2.imshow('image', img_convert)
cv2.waitKey(0)
cv2.destroyAllWindows()