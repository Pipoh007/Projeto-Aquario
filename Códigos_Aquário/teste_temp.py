import machine, onewire, ds18x20, time

ds_pin = machine.Pin(2)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    #print(rom)
    print(str(ds_sensor.read_temp(rom))+" C°")
    
  time.sleep(5)