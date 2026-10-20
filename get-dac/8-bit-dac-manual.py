import RPi.GPIO as g
g.setmode(g.BCM)
leds = [16, 20, 21, 25, 26, 17, 27, 22]
g.setup(leds, g.OUT)
dynamic_range = 3.3

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Динамическое напряжение выходит за динамический диапозон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)

def number_to_dac(number):
     buba = [int(element) for element in bin(number)[2:].zfill(8)]
     g.output(leds, buba)

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("ищак это не число\n")
finally:
    number_to_dac(0)
    g.cleanup()

