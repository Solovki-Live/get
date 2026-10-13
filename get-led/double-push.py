import RPi.GPIO as g
import time
g.setmode(g.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
g.setup(leds, g.OUT)
g.output(leds, 0)
up = 9
down = 10
g.setup(up, g.IN)
g.setup(down, g.IN)
num = 0
sleep_time = 0.2
promezhutok = 0.3
last_tap_up = 0
last_tap_down = 0

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
while True:
    proverka = False
    seychas = time.time()
    if g.input(up):
        if seychas - last_tap_down < promezhutok:
            num = 255
        else:
         if num < 255:
            
             num = num + 1
        last_tap_up = seychas
        proverka = True
        time.sleep(sleep_time)
    if g.input(down):
        if seychas - last_tap_up < promezhutok:
            num = 255
        else:
            if num > 0:
                num = num - 1
        proverka = True
        last_tap_down = seychas
              
        time.sleep(sleep_time)
    
    if proverka:
        print(num, dec2bin(num))
        g.output(leds, dec2bin(num))

    