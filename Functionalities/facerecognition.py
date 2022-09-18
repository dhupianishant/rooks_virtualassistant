import cv2
def Recognize():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    cap = cv2.VideoCapture(0)

    while True :
        ret, color_img = cap.read()
        gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_img)
        for (x,y,w,h) in faces:
            cv2.rectangle(color_img,(x,y), (x+w,y+h),(255,0,0),2)

        eyes = eye_cascade.detectMultiScale(gray_img)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(color_img,(ex,ey),(ex+ey,ey+eh),(0,255,0),2)
            print('Face detcted')

        cv2.imshow('img',color_img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
