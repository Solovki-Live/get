import RPi.GPIO as g
import time
g.setmode(g.BCM)
led = 26
g.setup(led, g.OUT)
pwm = g.PWM(led, 200)
duty = 0.0
pwm.start(duty)
while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty += 1.0
    if duty > 100:
        duty = 0.0