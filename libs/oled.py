########################################################################
# Feature: oled libs
# Author : Bing
# Version: 0.1
# Email  : kun1.huang@outlook.com
########################################################################
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306 as afs
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class OLED12864(object):
    def __init__(self, rst, dc, spi_port = 0, spi_device=0):
        self.RST = rst
        self.DC = dc
        self.SPI_PORT = spi_port
        self.SPI_DEVICE = spi_device
        self.__display = afs.SSD1306_128_64(rst=rst,dc=dc,spi=SPI.SpiDev(spi_port,spi_device,max_speed_hz=8000000))
        self.width = self.__display.width
        self.height = self.__display.height

    def showText(self, text, font='', font_size=12):
        if text == '':
            return
        imageFont = ImageFont.load_default()
        if font != '':
            imageFont = ImageFont.truetype(font, font_size)
        font_count = int(128/font_size)
        img = Image.new('1', self.width, self.height)
        draw = ImageDraw.Draw(img)
        lines = int(len(text)/font_count) + 1
        for i in range(0, lines):
            draw.text((0, i*font_size), text[i*font_count, (i+1)*font_count], imageFont, fill=1)
        self.__display.image(img)
        self.display()

    def showImage(self, src):
        if src == '':
            return
        img = Image.open('src').resize((128,64)).convert('1')
        self.__display.image(img)
        self.display()

    def clear(self):
        if self.__display:
            self.__display.clear()

    def display(self):
        if self.__display:
            self.__display.display()

    def begin(self):
        if self.__display:
            self.__display.begin()

    def clear_ex(self):
        self.begin()
        self.clear()
        self.display()

if __name__ == '__main__':
    oled = OLED12864(27, 22)
    oled.showText('Hello World')