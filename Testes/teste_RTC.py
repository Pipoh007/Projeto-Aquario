from machine import I2C, Pin
from ds1307 import DS1307
from pico_i2c_lcd import I2cLcd
import utime

i2c_lcd = I2C(id=1,scl=Pin(3),sda=Pin(2),freq=100000) # configuring and initializing the LCD display using I2C protocol.
lcd = I2cLcd(i2c_lcd, 0x27, 2, 16)

i2c_rtc = I2C(0,scl = Pin(1),sda = Pin(0),freq = 100000)  # We are also connecting the RTC module using I2C interface and hence we be using below
#line of code to configure it.

#Below code should be uncommented only to set the time for first time in RTC and then it should be commented back again.

'''
year = int(input("Year : "))
month = int(input("month (Jan --> 1 , Dec --> 12): "))
date = int(input("date : "))
day = int(input("day (1 --> monday , 2 --> Tuesday ... 0 --> Sunday): "))
hour = int(input("hour (24 Hour format): "))
minute = int(input("minute : "))
second = int(input("second : "))
now = (year,month,date,day,hour,minute,second,0)
rtc.datetime(now)
print(rtc.datetime())
'''

