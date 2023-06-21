import cv2

img = cv2.imread('lena.png')
img_hav = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

H = img_hav[:, :, 0]
S = img_hav[:, :, 1]
V = img_hav[:, :, 2]

H = H + 100
img_hav[:, :, 0] = H

img_hav1 = cv2.cvtColor(img_hav, cv2.COLOR_HSV2RGB)


cv2.imshow('slika', img_hav1)
cv2.waitKey(0)
cv2.destroyAllWindows()