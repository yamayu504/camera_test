import cv2
import sys
import time
import datetime

while True:
	now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
	cap = cv2.VideoCapture(0)
	rr, img =cap.read()
	cv2.imwrite( "/home/pi/camera_test/files/" + now + '.jpg', img)
	cap.release()
	time.sleep(600)

