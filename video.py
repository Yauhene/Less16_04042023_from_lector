import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# img = cv2.imread('face.jpg')
# krat = 0.2 # вводим коэффициент (масштаб)
# dim_list = list(img.shape)

# img = cv2.resize(img, (int(dim_list[1] * krat), int(dim_list[0] * krat)))
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Result', img_gray)
# cv2.waitKey(0)

# faces = face_cascades.detectMultiScale(img_gray)
# #print(faces)

# for (x, y, w, h) in faces:
#     #print(f'x = {x}, y = {y}, w = {w}, h = {h}')
#     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


# cv2.imshow('Result', img)
# cv2.waitKey(0)

#=========================================================
#cap = cv2.VideoCapture(0)  эта строка не сработала, заменена строкой ниже
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    _, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Result', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
