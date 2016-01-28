import RPi.GPIO as GPIO
import time
from pubnub import Pubnub

GPIO.setmode(GPIO.BCM)
led = 4
GPIO.setup(led, GPIO.OUT, initial=0)


pubnub.subscribe(channels='led-lights', callback-_callback, error=_error)

def _callback(m, channel):
  if m['led'] == 1:
    for i in range(7):
      GPIO.output(led, True)
      time.sleep(0.5)
      GPIO.output(led, False)
      time.sleep(0.5)
