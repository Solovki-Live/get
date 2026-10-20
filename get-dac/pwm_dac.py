import RPi.GPIO as g
#g.setmode(g.BCM)
#leds = [16, 20, 21, 25, 26, 17, 27, 22]
#g.setup(leds, g.OUT)
#dynamic_range = 3.3

class PWM_DAC:
    def __init__(self, g_pin, pwm_frequency, dynamic_range, verbose = False):
        self.g_pin = g_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        g.setmode(g.BCM)
        g.setup(self.g_pin, g.OUT, initial = 0)
        self.pwm = g.PWM(self.g_pin, self.pwm_frequency)
        self.pwm.start(0)
    def deinit(self):
        self.pwm.stop()
        g.output(self.g_bits, 0)
        g.cleanup()
    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print("Динамическое напряжение выходит за динамический диапозон ЦАП")
            print("Устанавливаем 0.0 В")
            return 0
        return int(voltage / self.dynamic_range * 100)
    def set_voltage(self, voltage):
        duty = self.voltage_to_number(voltage)
        self.pwm.ChangeDutyCycle(duty)

if __name__ == "__main__":
    dac = None
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
                    
            except ValueError:
                print("ищак это не число\n")
    finally:
        if dac is not None:

            dac.deinit()