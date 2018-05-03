#!/usr/bin/python3

"""
reference
* Getting started with Enviro pHAT
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat
* Raspberry PiでIFTTTのMaker WebhooksにPOSTする
https://qiita.com/undo0530/items/95dc85e3b58380ea359a
"""

import time
from datetime import datetime

import requests
from envirophat import light, motion, weather, leds

# define credentials in secret.py file
# IFTTT_EVENTNAME = ""
# IFTTT_KEY = ""
from secret import *

# IFTTT URL to POST
IFTTT_URL = 'https://maker.ifttt.com/trigger/{}/with/key/{}'.format(IFTTT_EVENTNAME, IFTTT_KEY)

print('Start posting to IFTTT')

try:
    while True:
        now = datetime.utcnow()
        lux = light.light()
        leds.on()
        r,g,b = light.rgb()
        leds.off()
        acc = motion.accelerometer()
        heading = motion.heading()
        temp = weather.temperature()
        press = weather.pressure(unit='hPa')
        data = {}
        data['value1'] = lux
        data['value2'] = temp
        data['value3'] = press
        requests.post(IFTTT_URL, json = data)
        print('Posted to IFTTT: {},{},{},{},{},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}'.format(
            now.strftime("%Y-%m-%d %H:%M:%S"), lux, r, g, b, acc.x, acc.y, acc.z, heading, temp, press))
        time.sleep(60)
except KeyboardInterrupt:
    leds.off()
    print('Stopped sending to IFTTT')
