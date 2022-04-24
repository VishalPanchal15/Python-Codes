from operator import truediv
import cv2
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while truediv:
    success, img = cap.read()
    faces = faceCascade.detectMultiScale(img, 1, 2, 4)
    for (x, y, w, h) in faces:
        # To make a face blurred
        ROI = img[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(ROI, (91,91), 0)

        #insert ROI back into image
        img[y:y+h, x:x+w] = blur
    if faces == ():
        cv2.putText(img, 'No Face Found!', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
    cv2.inshow('Face Blur', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
# Turn camera off
cap.release()

# Close camera window
cv2.destroyAllWindows()
