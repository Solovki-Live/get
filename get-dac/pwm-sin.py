import pwm_dac as r2r
import RPi.GPIO as g
import math
import time


amplitude = 3.2
sif = 10
po = 500
t = 0
saf = 1000
g.setmode(g.BCM)
try:
    dac = r2r.PWM_DAC(12, po, amplitude, True)
    while True:
        time.sleep(1/saf)
        t = t + 1/saf
        v_raw = math.sin(2 * math.pi * sif * t)
        v = (v_raw + 1) / 2 * amplitude
        print(f"Вольт: {v:.3f}")
        ans = dac.set_voltage(v)
        #print(f"Двоичность: {ans}")

        
finally:
    dac.deinit()
