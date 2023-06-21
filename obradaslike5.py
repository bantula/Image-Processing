import cv2

img = cv2.imread('negativ.png')

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


for i in range (0, img.shape[0]):
    for j in range (0, img.shape[1]):
      img[i, j] = 255 - img[i, j]

cv2.imshow('slika', img)
cv2.waitKey(0)
cv2.destroyAllWindows()