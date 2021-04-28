import RPi.GPIO as GPIO
import spidev
import time
spi = spidev.SpiDev()
spi.open(0,0)
def ReadChannel(channel):
adc = spi.xfer2([1,(8+channel)<<4,0])
data= ((adc[1]&3) << 8) + adc[2]
return data
def ConvertVolts(data,places):
volts = (data * 3.3) / float(1023)
volts = round(volts,places)
return volts
def ConvertTemp(data,places):
temp = ((data * 330)/float(1023))-5
temp = round(temp,places)
return temp
temp_channel = 0
delay = 3
while True:
temp_level = ReadChannel(temp_channel)
temp_volts = ConvertVolts(temp_level,2)
temp = ConvertTemp(temp_level,2)
print "____________________________________________"
print ("Temp : {} ({}V) {} deg C".format(temp_level,temp_volts,temp))
time.sleep(delay)