import RPi.GPIO as g
import time
g.setmode(g.BCM)
led = 26
g.setup(led, g.OUT)
surg = 6
g.setup(surg, g.IN)
while True:
    if g.input(surg):
        g.output(led, False)
    else:
        g.output(led, True)
    time.sleep(0.2)

