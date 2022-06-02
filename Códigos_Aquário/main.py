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
import dht #biblioteca para o sensor de umidade

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
        oled.text("Temp:",0,0)
        oled.text("Contagem:",0,24)
        sensorUmidade()
        sensorTemperatura()
        #sleep(1)
        print(contador-1)
        cont_string = str(contador-1)
        oled.text(cont_string, 73, 24, 1)
        oled.show()
        contador = contador - 1
        oled.fill(0)
        sleep(1)
        
        
        if contador == 0:
            i = 0
            oled.text(cont_string, 40, 24, 1)
            oled.show()
            led_onboard.value(1)
            while i<1:
                for position in range(3000,5000,50):
                    servoPin.duty_u16(position)
                    sleep(0.01)
                    print(position)
                sleep(1)
                for position in range(5000,3000,-50):
                    servoPin.duty_u16(position)
                    sleep(0.01)
                    print(position)
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
    
def sensorTemperatura():
    ds_pin = machine.Pin(2)
    ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

    roms = ds_sensor.scan()
    #print('Found DS devices: ', roms)


    ds_sensor.convert_temp()
    #time.sleep_ms(750)
    time.sleep_ms(10)

    for rom in roms:
        #print(rom)
      print(str(ds_sensor.read_temp(rom))+" C°")
      #oled.fill(0)
      #oled.text("Temperature:",0,0)
      oled.text(str(int(ds_sensor.read_temp(rom))) +" C",40,0)
      oled.show()
    
    time.sleep(1)

def sensorUmidade():
    sensorUmidade = dht.DHT11(Pin(4))
    #oled.fill(0)
    sensorUmidade.measure()
    #temp = str(sensorUmidade.temperature())
    hum = str(sensorUmidade.humidity())
    #oled.text("Temperature:",0,0)
    #oled.text(temp +" C",97,0)
    oled.text("Humidity:",0,10)
    oled.text(hum + " %",75,10)
    oled.show()
    #sleep(2)
    
# 4. Programa Principal

# 4.1 Timer  
timer_comida(6) # chamando a função, 6-1 segundos de contagem regressiva
sensorTemperatura()
# 4.2 servo Motor
