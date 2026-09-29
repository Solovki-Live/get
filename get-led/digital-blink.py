import RPi.GPIO as g
import time
g.setmode(g.BCM)
led = 26
g.setup(led, g.OUT)
state = 0
period = 1.0
while True:
    g.output(led, state)
    state = not state
    time.sleep(period)