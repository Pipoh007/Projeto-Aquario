# 1.Importações

from time import sleep
import time
import machine, onewire, ds18x20, time
from machine import Pin, SPI, I2C, PWM
#from machine import I2C, Pin
from ds1307 import DS1307
from ssd1306 import SSD1306_SPI
import utime
from utime import sleep_ms
import framebuf
from micropython import const
#import Adafruit_DHT
#import RPi.GPIO as GPIO

# 2. Declaração de Variáveis

# 2.1 Timer
led_onboard = machine.Pin(25, machine.Pin.OUT)

i2c_SPI = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
oled = SSD1306_SPI(128, 32, i2c_SPI, Pin(17),Pin(20), Pin(16))

i2c_rtc = I2C(0,scl = Pin(1),sda = Pin(0),freq = 100000)

rtc = machine.RTC()

# 2.2 Servo Motor
servoPin = PWM(Pin(12))
servoPin.freq(50)

# 3. Funções
def timer_comida(contador):
    contador_inicial = contador   
    while True: # pendente: converter segundos/valor numérico no formato de hora
        
        sleep(1)
        print(contador-1)
        cont_string = str(contador-1)
        oled.text(cont_string, 40, 24, 1)
        oled.show()
        contador = contador - 1
        oled.fill(0)
        
        if contador == 0:
            i = 0
            oled.text(cont_string, 40, 24, 1)
            oled.show()
            led_onboard.value(1)
            while (i < 2):              
              for degree in range(0,30,1):
                  servo(degree)
                  sleep(0.001)
                  print("increasing -- "+str(degree))
                
                  for degree in range(30, 0, -1):
                      servo(degree)
                      sleep(0.001)
                      print("decreasing -- "+str(degree))
                  i = i + 1
            sleep(1)
            led_onboard.value(0)
            oled.fill(0)
            contador = contador_inicial
    
def servo(degrees):
    if degrees > 180: degrees=180
    if degrees < 0: degrees=0
    
    maxDuty=9000
    minDuty=1000
    
    newDuty=minDuty+(maxDuty-minDuty)*(degrees/180)
    
    servoPin.duty_u16(int(newDuty))
    
# 4. Programa Principal

# 4.1 Timer  
timer_comida(6) # chamando a função, 6-1 segundos de contagem regressiva

# 4.2 servo Motor
