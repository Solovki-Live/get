import RPi.GPIO as g
import time
g.setmode(g.BCM)
led = 26
g.setup(led, g.OUT)
surg = 6
state = 0
g.setup(surg, g.IN)
while True:
    if g.input(surg):
        state = not state
        g.output(led, state)
        time.sleep(0.2)

