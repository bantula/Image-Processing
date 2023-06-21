import cv2

img = cv2.imread('binarizacija.png')

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

t = 125

for i in range (0, img.shape[0]):
    for j in range (0, img.shape[1]):
        if (img[i, j] < t ):
            img[i, j] = 0
        else :
            img[i, j] = 255

cv2.imshow('slika', img)
cv2.waitKey(0)
cv2.destroyAllWindows()