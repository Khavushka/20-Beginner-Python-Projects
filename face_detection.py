# Face detection using Python
# Install opencv-python package
# Du skal bruge et billede til at blive genkendt
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load image 
image = cv2.imread('image.jpg')

#Convert the image to grayscale
grayscale = cv2.cvColor(image, cv2.COLOR_BGR2GRAY)