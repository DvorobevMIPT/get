import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def decima2binare (value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

p=1

try:
    while (p>0):
        T = input()
        t = int(T)/510
        for i in range(256):
            GPIO.output(dac, decima2binare(i))
            print (i)
            time.sleep(t)
        for j in range (256):
            GPIO.output(dac, decima2binare(255-j))
            print (256-j)
            time.sleep(t)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()