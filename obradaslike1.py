import cv2

img = cv2.imread('lena.png')

green = img[:, :, 1]
blue = img[:, :, 2]
red = img[:, :, 0]

img2 = img
img[:, :, 0] = green
img[:, :, 1] = blue
img[:, :, 2] = red

cv2.imshow('slika', img)
cv2.waitKey(0)
cv2.destroyAllWindows()