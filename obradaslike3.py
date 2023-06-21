import cv2

img = cv2.imread('kontrast.png')

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

a = 150
b = 200

alpha = 1

for i in range (0, img.shape[0]):
    for j in range (0, img.shape[1]):
        if (img[i, j] < a ):
            img[i, j] = 0
        elif ((img[i, j] > a) and (img[i, j] < b)):
            img[i, j] = alpha * (img[i, j] - a)
        elif (img[i, j] > b):
            img[i, j] = 255
cv2.imshow('slika', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

