#!/usr/bin/python3

"""
reference
* Getting started with Enviro pHAT
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat

"""

import time
from datetime import datetime
from envirophat import light, motion, weather, leds

out = open('enviro.csv', 'w')
print('Start writing to file')
out.write('utctime,light,r,g,b,x,y,z,heading,temp,press\n')

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
        press = weather.pressure()
        out.write('{},{},{},{},{},{},{},{},{},{},{}\n'.format(
            now.strftime("%Y-%m-%d %H:%M:%S"), lux, r, g, b, acc.x, acc.y, acc.z, heading, temp, press))
        time.sleep(1)#yyyy-MM-dd HH:mm:ss
except KeyboardInterrupt:
    leds.off()
    out.close()
    print('Stopped writing to file')
