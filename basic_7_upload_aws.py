#!/usr/bin/python3

"""
reference
* Getting started with Enviro pHAT
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-enviro-phat
"""

import time, json
from datetime import datetime

import boto3

from envirophat import light, motion, weather, leds

# define credentials in secret.py file
# AWS_ACCESS_KEY_ID = ""
# AWS_SECRET_ACCESS_KEY = ""
# AWS_REGION = "us-east-1" #US East (N. Virginia)
from secret import *

client = boto3.client("iot-data")

response = client.publish(
    topic="pm/topic",
    qos=1,
    payload=json.dumps(payload, ensure_ascii=False))

s3 = boto3.resource('s3',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
#bucket = s3.Bucket(BUCKET_NAME)

print('Start uploading to Adafruit IO')

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
        aio.send('env1-lux', lux)
        aio.send('env1-temp', temp)
        aio.send('env1-press', press)
        print("Posted to Adafruit IO: {:.2f}, {:.2f}, {:.2f}".format(lux, temp, press))
        time.sleep(60)#yyyy-MM-dd HH:mm:ss
except KeyboardInterrupt:
    leds.off()
    print('Stopped uploading to Adafruit IO')
