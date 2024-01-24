import cv2

img = cv2.imread('1635072920195185343.png')
img = cv2.resize(img, dsize=(img.shape[1]//2, img.shape[0]//2))
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_edge = cv2.Canny(img1, threshold1=200, threshold2=200)

cv2.imshow('Hail to Hipnotoad', img)
cv2.imshow('Hail to Hipnotoad1', img_edge)
cv2.waitKey()
cv2.destroyAllWindows()