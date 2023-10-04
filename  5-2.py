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

def adc(troyka):
    k=0
    for i in range(7,-1,-1):
        k+= 2**i
        b = decima2binare(k)
        GPIO.output(dac, b)
        time.sleep(0.007)
        complanatorValue = GPIO.input(comp)
        
        if complanatorValue == 1:
            k =k - 2**i
    return k

bits = 8
levels = 2**bits
maxvoltage = 3.3

try:
    while True:
        value = decima2binare(adc(troyka))
        voltage = value / 256 * maxvoltage
        print('численное значение = ', value, 'напряжение = ', voltage)


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()