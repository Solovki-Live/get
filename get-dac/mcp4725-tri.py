import mcp4725_driver as mcp
import RPi.GPIO as g
import math
import time
import triangulation as tr


amplitude = 3.2
sif = 10

t = 0
saf = 1000
dr = 3.183
g.setmode(g.BCM)
try:
    dac = mcp.MCP4725(dr)
    while True:
        try:
            time.sleep(1/saf)
            t = t + 1/saf
            v_raw = tr.trian(sif, t)
            v = (v_raw + 1) / 2 * amplitude
            print(f"Вольт: {v:.3f}")
            ans = dac.set_voltage(v)
            #print(f"Двоичность: {ans}"
        except ValueError:
            pass

finally:
    dac.deinit()

