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
import struct

class OLED12864(object):
    def __init__(self, rst, dc, spi_port = 0, spi_device=0):
        self.RST = rst
        self.DC = dc
        self.SPI_PORT = spi_port
        self.SPI_DEVICE = spi_device
        self.__display = afs.SSD1306_128_64(rst=rst,dc=dc,spi=SPI.SpiDev(spi_port,spi_device,max_speed_hz=8000000))
        self.width = self.__display.width
        self.height = self.__display.height
        self.begin()

    def showText(self, text, font='', font_size=12):
        if text == '':
            return
        imageFont = ImageFont.load_default()
        if font != '':
            imageFont = ImageFont.truetype(font, font_size)
        imageFont.size = font_size
        font_count = int(128/font_size) * 2 + 2
        img = Image.new('1', (self.width, self.height))
        draw = ImageDraw.Draw(img)
        lines = []
        line = ""
        count = 0
        for s in text:
            if '\u4e00' <= s <= '\u9fff':
                count = count + 2
            else:
                count = count + 1
            print(s, count, font_count)
            if count > font_count: #超了
                lines.append(line)
                line = s
                count = font_count - count
            elif count == font_count:
                line += s
                lines.append(line)
                count = 0
                line =  ""
            else:
                line += s
        if count < font_count:
            lines.append(line)
        # lines = int(len(text)/font_count) + 1
        y = 0
        print(lines)
        for l in lines:
            draw.text((0, y * font_size), l, font=imageFont, fill=1)
            y = y + 1
        self.__display.image(img)
        self.display()

    def showImageFile(self, file):
        if file == '':
            return
        img = Image.open(file).resize((128,64)).convert('1')
        self.__display.image(img)
        self.display()
    def showImage(self, data, mode, width, height):
        if data == None:
            return
        img = Image.frombuffer(mode, (width, height), data).resize((128,64)).convert('1')
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
    oled = OLED12864(17, 22)
    oled.showText('Hello World! this is a test, 这可能真的是一个测试呢！', 'msyh.ttc')