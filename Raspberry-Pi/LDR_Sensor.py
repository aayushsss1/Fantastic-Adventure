import spidev
import time
spi = spidev.SpiDev()
spi.open(0,0)
def ReadChannel(channel):
adc = spi.xfer2([1,(8+channel)<<4,0]) #as per datasheet
data= ((adc[1]&3) << 8) + adc[2]
return data
def ConvertVolts(data,places):
volts = (data * 3.3) / float(1023)
volts = round(volts,places)
return volts
Light_channel = 0 ##connect with A0
delay = 3
while True:
Light_level = ReadChannel(Light_channel)
Light_volts = ConvertVolts(Light_level,2)
print "____________________________________________"
print ("Light Value: {} ({}V)".format(Light_level, Light_volts))
time.sleep(delay)