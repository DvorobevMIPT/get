import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def decima2binare (value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def if_float(number):
    number = [str(i) for i in number]
    if number.count('.') == 1:
        tar = number.index('.')
    if number[0] == '-':
        number = str(''.join(number))
    if number.isdigit():
        return True
    return False

def if_negative(number):
    number = str(number)
    if number[0] == '-':
        if number[1:].isdigit():
            return True
    return False 


p=1 

try:
    while (p>0):
        decima = input()
        if (decima == 'q'):
            sys.exit()
            print(type(decima))
        elif if_float(decima):
            print('это не целое число')
        elif if_negative(decima):
            print("это отрицательное число")
        elif (float(decima) > 255):
            print("Ввод значения превышаюшего возможности 8-разрядного ЦАП")
        else:
            volt = 3.3 * int(decima) / 256
            print ("Предполагаемое напряжение на ЦАП = ", volt, "Вольт")
            GPIO.output(dac,decima2binare(int(decima)))
            

        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()