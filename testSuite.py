import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)

while True:
	print("blinking LED for 5 seconds at 500ms intervals")
	for v in range(0,5):
		GPIO.output(11, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(11, GPIO.LOW)
		time.sleep(0.5)

	print("Printing light sensor values for 5 seconds")
	for w in range(0,50):
		value = mcp.read_adc(0)
		light = ""
		if value> 500:
			print("light: %d" % (value))
		else:
			print("dark: %d" % (value))
		
		time.sleep(.1)
	
	print("Blinking light 4 times at 200ms intervals")
	for x in range(0,4):
		GPIO.output(11, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(11, GPIO.LOW)
		time.sleep(0.2)
	
	print("reading sound sensor, LED on if ADC reads above 500")
	for y in range(0,50):
		value = mcp.read_adc(0)
		if value> 500:
			GPIO.output(11, GPIO.HIGH)
		
		print(value)
		time.sleep(.1)
		GPIO.output(11,GPIO.LOW)

	print("Blinking light 4 times at 200ms intervals")
	for z in range(0,4):
		GPIO.output(11, GPIO.HIGH)
		time.sleep(0.2)
		GPIO.output(11, GPIO.LOW)
		time.sleep(0.2)
