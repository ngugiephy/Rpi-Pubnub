##################
#### pnLED.py ####
##################

from Pubnub import Pubnub
import RPi.GPIO as GPIO ## Import GPIO library

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

GPIO.setup(21, GPIO.OUT) ## Setup GPIO Pin 17 to OUT - Green
GPIO.setup(20, GPIO.OUT) ## Setup GPIO Pin 18 to OUT - Yellow
GPIO.setup(16, GPIO.OUT) ## Setup GPIO Pin 27 to OUT - Red

GPIO.output(21,False) ## Turn on GPIO pin 17
GPIO.output(20,False) ## Turn on GPIO pin 18
GPIO.output(16,False) ## Turn on GPIO pin 27

# Enter your PubNub Publish Key and use the Market Order Demo Subscribe Key
pubnub = Pubnub(publish_key="pub-c-1afde382-1404-4079-9139-8196509ba945", subscribe_key="sub-c-f2b8c5c0-c34b-11e5-b684-02ee2ddab7fe", ssl_on=False)

# Listen for Messages on the Market Order Channel
channel = 'pubnub-market-orders'

def callback(message, channel):
    print(message['order_quantity']) # Use the Order Quantity value as the LED trigger
    
    # Reset LEDs to OFF
    GPIO.output(21,False)
    GPIO.output(20,False)
    GPIO.output(16,False)
    
    if (message['order_quantity'] >= 100) and (message['order_quantity'] < 200):
        GPIO.output(21,True) # Turn on GREEN
    elif (message['order_quantity'] >= 200) and (message['order_quantity'] < 400):
        GPIO.output(20,True) # Turn on YELLOW
    elif (message['order_quantity'] >= 400):
        GPIO.output(16,True) # Turn on RED

def error(message):
    print("ERROR : " + str(message))

def connect(message):
    print("CONNECTED")

def reconnect(message):
    print("RECONNECTED")

def disconnect(message):
    print("DISCONNECTED")

pubnub.subscribe(channel, callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)
