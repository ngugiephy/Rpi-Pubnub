##    ngugiephy
##
##  simple led blink for the raspberry pi

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 4
GPIO.setup(led, GPIO.OUT, initial=0)

try:
  while True:
    GPIO.output(led, 1)
    time.sleep(0.1)
    GPIO.output(led, 0)
    time.sleep(0.1)
    
finally:
  GPIO.cleanup()
