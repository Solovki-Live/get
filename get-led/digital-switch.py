import RPi.GPIO as g
import time
g.setmode(g.BCM)
led = 26
g.setup(led, g.OUT)
button = 13
state = 0
g.setup(button, g.IN)
while True:
    if g.input(button):
        state = not state
        g.output(led, state)
        time.sleep(0.2)
