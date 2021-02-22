import sys
import os
sys.path.append("/home/pi/git/bingiot")
from libs import OLED12864
from picamera import PiCamera 
class CameraOLED(object):
    def __init__(self, rst, dc, width, height):
        self.oled = OLED12864(rst, dc)
        self.width = width
        self.height = height
    def write(self, data):
        self.oled.showImage(data, "L", self.width, self.height)

def main():
    camera = PiCamera()
    oled = CameraOLED(17, 22, 1920, 1088)
    camera.capture(oled, "raw", resize=(oled.width, oled.height))

if __name__ == "__main__":
    main()