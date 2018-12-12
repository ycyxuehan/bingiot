from picamera import PiCamera 
from time import sleep 
camera = PiCamera() 
camera.start_preview()
camera.capture('test.jpg')

camera.stop_preview()