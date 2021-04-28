import time
#import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
#DC = 23
#SPI_PORT = 0
#SPI_DEVICE = 0
# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0
# 128x32 display with hardware I2C:

#disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST,i2c_address=0x3C)
# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT,
SPI_DEVICE, max_speed_hz=8000000))
# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT,
SPI_DEVICE, max_speed_hz=8000000))
# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()
width=disp.width
height=disp.height
image=Image.new('1',(width,height))
draw=ImageDraw.Draw(image)
draw.rectangle((0,0,width,height),outline=0,fill=0)
padding=0
top=padding
x=padding
font=ImageFont.load_default()
draw.text((x,top),'Initializing', font=font,fill=1)
draw.text((x,top+20),'Aayush Subramaniam', font=font, fill=1)
disp.image(image)
disp.display()
time.sleep(5)