#!/usr/bin/python3

"""
reference
* Getting started with Enviro pHAT
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat
* Adafruit IO: The Internet of Things for Everyone
https://learn.adafruit.com/adafruit-io/overview
https://github.com/adafruit/io-client-python/tree/master/examples
"""

# Import Adafruit IO REST client.
from Adafruit_IO import Client

from envirophat import light, motion, weather, leds

# define credentials in secret.py file
# ADAFRUIT_IO_KEY = ""
# ADAFRUIT_IO_USER = ""
from secret import *

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USER, ADAFRUIT_IO_KEY)

print('Start uploading to Adafruit IO')

lux = light.light()
temp = weather.temperature()
press = weather.pressure(unit='hPa')
aio.send('env1_lux', lux)
aio.send('env1_temp', temp)
aio.send('env1_press', press)
print("Posted to Adafruit IO: {:.2f}, {:.2f}, {:.2f}".format(lux, temp, press))
