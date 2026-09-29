import RPi.GPIO as g
import time
g.setmode(g.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
g.setup(leds, g.OUT)
g.output(leds, 0)
light_time = 0.2
for led in leds:
    g.output(led, 1)
    time.sleep(light_time)
    g.output(led, 0)
for led in reversed(leds):
    g.output(led, 1)
    time.sleep(light_time)
    g.output(led, 0)