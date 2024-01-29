import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# camera = cv2.VideoCapture(0)
camera = cv2.VideoCapture('BMW X5M vs ML63 AMG II ШАШКИ В МОСКВЕ II COMBO VINE.mp4')

if camera.isOpened():
    print('ok')
else:
    print('not ok')


for i in range(10000):
    bul, stream = camera.read()
    gray_stream = cv2.cvtColor(stream, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_stream, scaleFactor=1.5, minNeighbors=7)
    for (x, y, w, h) in faces:
        cv2.rectangle(stream, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # out.write(stream)
    cv2.imshow('window', stream)
    # cv2.waitKey(33)
    if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == 27:  # 27 это escape
        break

camera.release()
# cv2.waitKey(0)
cv2.destroyAllWindows()