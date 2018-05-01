import time
from envirophat import light, motion, weather, leds

print('light\trgb\tmotion\theading\ttemp\tpress\n')

while True:
    lux = light.light()
    leds.on()
    rgb = str(light.rgb())[1:-1].replace(' ', '')
    leds.off()
    acc = str(motion.accelerometer())[1:-1].replace(' ', '')
    heading = motion.heading()
    temp = weather.temperature()
    press = weather.pressure()
    print('%f\t%s\t%s\t%f\t%f\t%f\n' % (lux, rgb, acc, heading, temp, press))
    time.sleep(1)
