import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# 引脚配置，按照上面的接线来配置
RST=5
DC=6
# 因为连的是CE0，这里的PORT和DEVICE也设置为0
SPI_PORT=0
SPI_DEVICE=0

#根据自己的oled型号进行初始化，我的是128X64、SPI的oled，使用SSD1306_128_64初始化
disp=Adafruit_SSD1306.SSD1306_128_64(rst=RST,dc=DC,spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE,max_speed_hz=8000000))

disp.begin()
disp.clear()
disp.display() #清屏

#image 1，绘制了几个图形
width=disp.width
height=disp.height
image1=Image.new('1',(width,height)) #新建一个128X64的二值图像对象
draw1=ImageDraw.Draw(image1) #获取image1的draw对象

padding=1
shape_width=50
left=padding
top=padding
right=width-padding
bottom=height-padding
x=padding

draw1.rectangle((left,top,right,bottom),outline=1,fill=0) #画矩形
draw1.ellipse((left+10,top+10,left+10+shape_width,top+10+shape_width),outline=1,fill=0) #画椭圆
draw1.polygon([(right-20,top+10),(width/2+5,bottom-10),(right-5,bottom-10)],outline=1,fill=0) #画三角

# image 2，载入一副图片
image2=Image.open('ironman.jpeg').resize((128,64)).convert('1')

# image 3，显示一些文字
image3=Image.new('1',(width,height))
draw3=ImageDraw.Draw(image3)
font1=ImageFont.load_default()
font2=ImageFont.truetype('DejaVuSans.ttf',15)
font3=ImageFont.truetype('DejaVuSans.ttf',18)
draw3.text((0,0),'Hello',font=font1,fill=1)
draw3.text((0,15),'World!',font=font2,fill=1)
draw3.text((0,35),'Enjoy it!',font=font3,fill=1)

try:
    index=1
    while True: #循环显示
        if index==1:
            disp.image(image1)
            index+=1
        elif index==2:
            disp.image(image2)
            index+=1
        else:
            disp.image(image3)
            index=1
        disp.display()
        time.sleep(2)
except:
    disp.clear()
    disp.display()