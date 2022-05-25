from time import sleep
import machine
from machine import Pin, SPI
from machine import I2C, Pin
from ds1307 import DS1307
from ssd1306 import SSD1306_SPI

led_onboard = machine.Pin(25, machine.Pin.OUT)

i2c_SPI = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
oled = SSD1306_SPI(128, 32, i2c_SPI, Pin(17),Pin(20), Pin(16))

i2c_rtc = I2C(0,scl = Pin(1),sda = Pin(0),freq = 100000)

rtc = machine.RTC()

cont = 6
while True:
    sleep(1)
    print(cont-1)
    cont_string = str(cont-1)
    oled.text(cont_string, 40, 24, 1)
    oled.show()
    cont = cont - 1
    oled.fill(0)
    
    if cont == 0:
        
        oled.text(cont_string, 40, 24, 1)
        oled.show()
        led_onboard.value(1)
        sleep(1)
        led_onboard.value(0)
        oled.fill(0)
        cont = 6
        
        
