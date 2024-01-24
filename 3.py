'''
numpy - массивы и матрицы
pandas - работа с таблицами
opencv - работа с графикой в нейросетях
tensorflow - для обучения нейросетей
keras - для теста готовых нейросетей
'''

import cv2

img = cv2.imread('1635072920195185343.png')
print(img)
# вывод картинки
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyWindow('Image')
# print(img.shape)

# изменили размер
# img_resize = cv2.resize(img, dsize=(img.shape[1]//3, img.shape[0]//3))  # ширина и высота в другом порядке
# cv2.imshow('Image', img_resize)
# cv2.waitKey(0)
# cv2.destroyWindow('Image')

# развернуть картинку
# img_v = cv2.flip(img_resize, 1)
# img_h = cv2.flip(img_resize, 0)
# img_vh = cv2.flip(img_resize, -1)
# cv2.imshow('Image1', img_v)
# cv2.imshow('Image2', img_h)
# cv2.imshow('Image3', img_vh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# поворот картинки
width = img.shape[1]
height = img.shape[0]
center = (width//2, height//2)
print(center)

for i in range(0, 360, 10):
    matrix_rot = cv2.getRotationMatrix2D(center, i, 1)
    img_rot = cv2.warpAffine(img, matrix_rot, dsize=(width, height))
    cv2.imshow('Image', img_rot)
    cv2.waitKey(500)
    cv2.destroyAllWindows()