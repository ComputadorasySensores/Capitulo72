import mraa
import time

led = mraa.Pwm(11)
 
led.period_us(700)
 
led.enable(True)

value= 1.0
 
while True:
	led.write(value)
	time.sleep(0.05)
	value = value - 0.01
	if value <= 0:
    		value = 1.0
