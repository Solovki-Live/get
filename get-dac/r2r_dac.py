import RPi.GPIO as g
#g.setmode(g.BCM)
#leds = [16, 20, 21, 25, 26, 17, 27, 22]
#g.setup(leds, g.OUT)
#dynamic_range = 3.3

class R2R_DAC:
    def __init__(self, g_bits, dynamic_range, verbose = False):
        self.g_bits = g_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        g.setmode(g.BCM)
        g.setup(self.g_bits, g.OUT, initial = 0)
    def deinit(self):
        g.output(self.g_bits, 0)
        g.cleanup()
    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print("Динамическое напряжение выходит за динамический диапозон ЦАП")
            print("Устанавливаем 0.0 В")
            return 0
        return int(voltage / self.dynamic_range * 255)
    def number_to_dac(self, number):
        buba = [int(element) for element in bin(number)[2:].zfill(8)]
        g.output(self.g_bits, buba)
    def set_voltage(self, voltage):
        self.number_to_dac(self.voltage_to_number(voltage))
if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
                    
            except ValueError:
                print("ищак это не число\n")
    finally:
        dac.deinit()