#!/usr/bin/python3

"""
reference
* Getting started with Enviro pHAT
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat
"""

import time
from datetime import datetime
from envirophat import light, motion, weather, leds

print('utctime,light,r,g,b,x,y,z,heading,temp,press')

while True:
    now = datetime.utcnow()
    lux = light.light()
    leds.on()
    r,g,b = light.rgb()
    leds.off()
    acc = motion.accelerometer()
    heading = motion.heading()
    temp = weather.temperature()
    press = weather.pressure()
    print('{},{},{},{},{},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}'.format(
        now.strftime("%Y-%m-%d %H:%M:%S"), lux, r, g, b, acc.x, acc.y, acc.z, heading, temp, press))
    time.sleep(1)#yyyy-MM-dd HH:mm:ss