import math

def CelToFahr(celsius):
    return (celsius * 9/5) + 32

def min(a, b):
    return a if a < b else b

def VolumeOfSphere(radius):
    return (4/3) * math.pi * radius**3

print("25°C to Fahrenheit:", CelToFahr(25))
print("Minimum of 10 and 20:", min(10, 20))
print("Volume of sphere with radius 3:", VolumeOfSphere(3))
