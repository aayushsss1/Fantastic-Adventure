import RPi.GPIO as GPIO
import time
import sys
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_MCP230xx')
from Adafruit_MCP230XX import Adafruit_MCP230XX
mcp=Adafruit_MCP230XX(busnum=1, address=0x20, num_gpios=16)
mcp.config(0,mcp.OUTPUT)
##mcp.config(1,mcp.OUTPUT)
##mcp.config(2,mcp.OUTPUT)
##mcp.config(3,mcp.OUTPUT)
mcp.config(4,mcp.OUTPUT)
##mcp.config(5,mcp.OUTPUT)
##mcp.config(6,mcp.OUTPUT)
##mcp.config(7,mcp.OUTPUT)
mcp.config(8,mcp.OUTPUT)
while True:
mcp.output(0,1)
mcp.output(4,1)
mcp.output(8,1)
time.sleep(1)
mcp.output(0,0)
mcp.output(4,0)
mcp.output(8,0)
time.sleep(1)