import cv2
def detect(path):
    detected_faces=[]
    im=cv2.imread(path)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
	face = gray[y:y + h, x:x + w]
	face_resize = cv2.resize(face, (width, height))
	detected_faces.append(face_resize)
    return detected_faces
