import cv2
import math

img = cv2.imread('soba.png')

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

k = 50
c = 255 / (math.log(k * 255))

for i in range (0, img.shape[0]):
    for j in range (0, img.shape[1]):
        img[i, j] = c * (1 + math.log(k*img[i, j]))


cv2.imshow('slika', img)
cv2.waitKey(0)
cv2.destroyAllWindows()