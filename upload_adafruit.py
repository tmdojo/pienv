#!/usr/bin/python3

"""
reference
* Getting started with Enviro pHAT
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat
* Adafruit IO: The Internet of Things for Everyone
https://learn.adafruit.com/adafruit-io/overview
https://github.com/adafruit/io-client-python/tree/master/examples
"""
import time, json
from datetime import datetime

import requests

# Import Adafruit IO REST client.
from Adafruit_IO import Client

from envirophat import light, motion, weather, leds

# define credentials in secret.py file
# ADAFRUIT_IO_KEY = ""
# ADAFRUIT_IO_USER = ""
from secret import *

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USER, ADAFRUIT_IO_KEY)

#TODO: didn't managed to get api key restriction working
# currently POST method is set not to require api Key
# something to do with CORS?
# https://forums.aws.amazon.com/message.jspa?messageID=658389
headers = {'x-api-key': AWS_ENDPOINT_APIKEY}

now = datetime.utcnow()
lux = light.light()
leds.on()
r,g,b = light.rgb()
leds.off()
acc = motion.accelerometer()
heading = motion.heading()
temp = weather.temperature()
press = weather.pressure(unit='hPa')

print('Start uploading to Adafruit IO')
aio.send('env1-lux', lux) # 1st argument must be feed key, not feed name
aio.send('env1-temp', temp)
aio.send('env1-press', press)
print("Posted to Adafruit IO: {:.2f}, {:.2f}, {:.2f}".format(lux, temp, press))

payload = {}
payload['datetime']=now.timestamp() # datetime object is not json stringfyable. Use epoch
payload['env1-lux']=lux
payload['env1-temp']=temp
payload['env1-press']=press
r = requests.post(AWS_ENDPOINT, json=payload, headers=headers)
print("Posted to AWS Endpoint: {}".format(r.text))
