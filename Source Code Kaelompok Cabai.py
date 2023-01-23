from machine import Pin
from time import sleep
import dht 

sensor = dht.DHT22(Pin(14))
while True:
  try:
    sensor.measure()
    temp = sensor.temperature() /20 - 10
    hum = sensor.humidity() / 20 -10
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('=============')
