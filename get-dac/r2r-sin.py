import r2r_dac as r2r

import math
import time


amplitude = 3.2
sif = 10
t = 0
saf = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], amplitude, True)
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
