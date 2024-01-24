import cv2

img = cv2.imread('1635072920195185343.png')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

imgs = [img, img1, img2, img3]

while True:
    for i in imgs:
        cv2.imshow('Hail to Hipnotoad', i)
        cv2.waitKey(500)
        # cv2.destroyAllWindows()
