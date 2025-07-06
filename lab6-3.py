from adafruit_circuitplayground import cp
import time

def CelToFahr(c):
    return (c * 9 / 5) + 32

while True:
    if cp.button_a:
        temp = cp.temperature
        if cp.switch:
            print("Temperature in Fahrenheit:", CelToFahr(temp))
        else:
            print("Temperature in Celsius:", temp)
        time.sleep(0.5)
