from adafruit_circuitplayground import cp
import time

def CelToFahr(celsius):
    return (celsius * 9 / 5) + 32

while True:
    temp = cp.temperature
    if cp.switch:
        print("Temperature in Fahrenheit:", CelToFahr(temp))
    else:
        print("Temperature in Celsius:", temp)
    time.sleep(1)
