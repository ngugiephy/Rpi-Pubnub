import sys
from pubnub import Pubnub

pubnub = Pubnub(publish_key='', subscribe_key='')

channel = "hello-pi"

data = {
  'username': 'ngugiephy',
  'message' : "hey there, it's ngugephy"
  }
def callback(m):
  print(m)
  
pubnub.publish(channel, data, callback=callback, error=callback)
  
