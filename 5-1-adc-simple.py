import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decima2binare (value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = decima2binare(value)
    GPIO.output(dac,signal)
    return signal

bits = 8
levels = 2**bits
maxvoltage = 3.3

try:
    while True:
        for value in range(256):
            time.sleep(0.0007)
            signal = num2dac(value)
            voltage = value / levels * maxvoltage
            complanatorValue = GPIO.input(comp)
            if complanatorValue == 0:
                print('численное значение = ', value, 'напряжение = ', voltage)
                break

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()