import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(18,GPIO.IN)
print(GPIO.input(12))
print(GPIO.input(15))
print(GPIO.input(16))
print(GPIO.input(18))


x= (GPIO.input(12)<<3)+(GPIO.input(15)<<2)+(GPIO.input(16)<<1)+(GPIO.input(18)<<0)

print(x)

