import cv2

face = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face.detectMultiScale(gray)

for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)

cv2.imwrite("output.jpg", img)
