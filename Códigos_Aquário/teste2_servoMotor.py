from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(12))
pwm.freq(50)

i=0

while i<1:
    for position in range(3000,5000,50):
        pwm.duty_u16(position)
        sleep(0.01)
        print(position)
    for position in range(5000,3000,-50):
        pwm.duty_u16(position)
        sleep(0.01)
        print(position)
    i = i + 1