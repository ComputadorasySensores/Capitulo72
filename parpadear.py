import mraa
import time

led1 = mraa.Gpio(18)	
led1.dir(mraa.DIR_OUT)

while True:
	led1.write(1)
	time.sleep(1)
	led1.write(0)
	time.sleep(1)
