import time
from envirophat import light, motion, weather, leds

print('light,r,g,b,x,y,z,heading,temp,press')

while True:
    lux = light.light()
    leds.on()
    r,g,b = light.rgb()
    leds.off()
    acc = motion.accelerometer()
    heading = motion.heading()
    temp = weather.temperature()
    press = weather.pressure()
    #print('{},{},{},{},{},{},{},{},{},{}'.format(lux, r, g, b, acc.x, acc.y, acc.z, heading, temp, press))
    print('{},{},{},{},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}'.format(lux, r, g, b, acc.x, acc.y, acc.z, heading, temp, press))
    time.sleep(1)
