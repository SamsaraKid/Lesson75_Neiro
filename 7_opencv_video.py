import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

camera = cv2.VideoCapture(0)
# camera = cv2.VideoCapture('имя файла')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videocapture.avi', fourcc, 10, (640, 480))

if camera.isOpened():
    print('ok')
else:
    print('not ok')


for i in range(100):
    bul, stream = camera.read()
    gray_stream = cv2.cvtColor(stream, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_stream, scaleFactor=1.1, minNeighbors=10)
    for (x, y, w, h) in faces:
        cv2.rectangle(stream, (x, y), (x + w, y + h), (255, 0, 0), 2)
    out.write(stream)
    cv2.imshow('window', stream)
    cv2.waitKey(33)
    if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == 27:  # 27 это escape
        break

camera.release()
# cv2.waitKey(0)
cv2.destroyAllWindows()