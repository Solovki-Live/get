import RPi.GPIO as g
import time
g.setmode(g.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
g.setup(leds, g.OUT)
g.output(leds, 0)
up = 9
down = 10
g.setup(up, g.IN)
g.setup(down, g.IN)
num = 0
sleep_time = 0.2

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
while True:
    proverka = False
    if g.input(up):
        if num < 255:
            
            num = num + 1
            proverka = True
            time.sleep(sleep_time)
    if g.input(down):
        if num > 0:
           proverka = True
           num = num - 1
           time.sleep(sleep_time)
    
    if proverka:
        print(num, dec2bin(num))
        g.output(leds, dec2bin(num))

    