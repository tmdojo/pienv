#!/usr/bin/python3

"""
reference
* Getting started with Enviro pHAT
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat
"""

import time, json
from datetime import datetime

import requests
from envirophat import light, motion, weather, leds

# define credentials in secret.py file
# AWS_ACCESS_KEY_ID = ""
# AWS_SECRET_ACCESS_KEY = ""
# AWS_REGION = "us-east-1" #US East (N. Virginia)
# AWS_ENDPOINT = "" # API ENDPOINT to run lambda functions
from secret import *

now = datetime.utcnow()
lux = light.light()
leds.on()
r,g,b = light.rgb()
leds.off()
acc = motion.accelerometer()
heading = motion.heading()
temp = weather.temperature()
press = weather.pressure(unit='hPa')

#TODO: didn't managed to get api key restriction working
# currently POST method is set not to require api Key
# something to do with CORS?
# https://forums.aws.amazon.com/message.jspa?messageID=658389
headers = {'x-api-key': AWS_ENDPOINT_APIKEY}

payload = {}
payload['datetime']=now.timestamp() # datetime object is not json stringfyable. Use epoch
payload['env1-lux']=lux
payload['env1-temp']=temp
payload['env1-press']=press
r = requests.post(AWS_ENDPOINT, json=payload, headers=headers)
print("Posted to AWS Endpoint: {:.2f}, {:.2f}, {:.2f}".format(lux, temp, press))
