import math

# Convert Celsius to Fahrenheit
def CelToFahr(celsius):
    return (celsius * 9/5) + 32

# Return minimum of two values
def min(a, b):
    return a if a < b else b

# Volume of a sphere
def VolumeOfSphere(radius):
    return (4/3) * math.pi * radius**3

# Test your functions
print("25°C to Fahrenheit:", CelToFahr(25))
print("Minimum of 10 and 20:", min(10, 20))
print("Volume of sphere with radius 3:", VolumeOfSphere(3))
