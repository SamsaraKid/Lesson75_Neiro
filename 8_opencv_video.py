import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
camera = cv2.VideoCapture('BMW X5M vs ML63 AMG II ШАШКИ В МОСКВЕ II COMBO VINE.mp4') #видеозахват
if camera.isOpened():
    print('ok')
else:
    print('neok')

for i in range(10000): #100 кадров
    print(camera.read())
    k1, k2 = camera.read() #k1=True, k2=кадр в виде матрицы
    gray_image = cv2.cvtColor(k2, cv2.COLOR_BGR2GRAY)
    numbers = face_cascade.detectMultiScale(gray_image, 1.3, 5)
    for i, (x, y, w, h) in enumerate(numbers):
        roi_color = k2[y:y + h, x:x + w]
        cv2.putText(k2, str(x) + " " + str(y) + " " + str(w) + " " + str(h), (480, 220), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255))
        r = 400.0 / roi_color.shape[1]
        dim = (400, int(roi_color.shape[0] * r))
        resized = cv2.resize(roi_color, dim, interpolation=cv2.INTER_AREA)
        w_resized = resized.shape[0]
        h_resized = resized.shape[1]

        k2[100:100 + w_resized, 100:100 + h_resized] = resized  # Собираем в основную картинку
        cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('Video_Numer_Znak.jpg', resized)  # сохранить только знак
    # Отображение результирующего кадра
    cv2.imshow('Video', k2)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('Video_Numer_det.jpg', k2)  # сохранить автомобиль и знак
    if cv2.waitKey(1) & 0xFF == 27:
       break

camera.release() #отключение от камеры
# cv2.waitKey(0)
cv2.destroyAllWindows()