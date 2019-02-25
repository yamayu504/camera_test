import cv2
import sys
import time
import datetime
import os
import boto3

image_bucket_name = "sayang-images"
s3 = boto3.resource('s3')
while True:
	now = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
	date = datetime.date.today().strftime("%y%m%d")
	cap = cv2.VideoCapture(0)
	rr, img =cap.read()
	fileName = now + '.jpg'
	cv2.imwrite("/home/pi/camera_test/files/" + fileName, img)
	time.sleep(2)  
	#s3 uploder
	s3.Bucket(image_bucket_name).upload_file("/home/pi/camera_test/files/" + fileName, "images/" + date + "/" +fileName, ExtraArgs={'ContentType': 'image/jpeg'})
	
	#dropbox upload 
	os.system("/home/pi/camera_test/db_uploader/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/camera_test/files/"+ fileName +" /SayangApp/"+ date +"/" )
	cap.release()
	time.sleep(600)
