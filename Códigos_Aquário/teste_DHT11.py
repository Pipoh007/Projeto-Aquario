from machine import Pin, SPI
from time import sleep
import dht
from ssd1306 import SSD1306_SPI

spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
oled = SSD1306_SPI(128, 32, spi, Pin(17),Pin(20), Pin(16))
sensorUmidade = dht.DHT11(Pin(4)) 
 
while True:
    oled.fill(0)
    sensorUmidade.measure()
    temp = str(sensorUmidade.temperature())
    hum = str(sensorUmidade.humidity())
    oled.text("Temperature:",0,0)
    oled.text(temp +" C",97,0)
    oled.text("Humidity:",0,10)
    oled.text(hum + " %",75,10)
    oled.show()
    sleep(2)
'''    
import dht
import machine
from time import sleep
SENSOR_PIN = 4
sensor = dht.DHT11(machine.Pin(SENSOR_PIN, machine.Pin.IN, machine.Pin.PULL_UP))

sensor.measure()
temperatura = sensor.temperature()
humidade = sensor.humidity()

print('Temperatura', temperatura)
print('Humidade', humidade)
'''