import cv2
import sys
import time
import datetime
import os

while True:
	now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
	cap = cv2.VideoCapture(0)
	rr, img =cap.read()
	fileName = "/home/pi/camera_test/files/" + now + '.jpg'
	cv2.imwrite( fileName, img)
	os.system('/home/pi/camera_test/db_uploader/Dropbox-Uploader/dropbox_uploader.sh upload '+ fileName +' /SayangApp/')
	cap.release()
	time.sleep(600)
