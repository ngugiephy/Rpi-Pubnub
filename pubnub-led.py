import RPi.GPIO as GPIO
import time
from pubnub import Pubnub
import sys

GPIO.setmode(GPIO.BCM)
led = 4
GPIO.setup(led, GPIO.OUT, initial=0)

pubnub = Pubnub(publish_key='pub-c-1afde382-1404-4079-9139-8196509ba945', subscribe_key='sub-c-f2b8c5c0-c34b-11e5-b684-02ee2ddab7fe')
channel = 'led-lights'



def _callback(m, channel):
  print(m)
  if m['led'] == 1:
    for i in range(7):
      GPIO.output(led, True)
      time.sleep(0.5)
      GPIO.output(led, False)
      time.sleep(0.5)
      
def _error(m):
  print(m)

pubnub.subscribe(channels=channel, callback-_callback, error=_error)
