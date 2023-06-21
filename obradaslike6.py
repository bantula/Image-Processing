import cv2

img = cv2.imread('bubreg.png')

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

a = 130
b = 240

for i in range (0, img.shape[0]):
    for j in range (0, img.shape[1]):
        if (img[i, j] > a and img[i, j] < b):
            img[i, j] = 255

cv2.imshow('slika', img)
cv2.waitKey(0)
cv2.destroyAllWindows()