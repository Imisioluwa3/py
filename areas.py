import math
import os

def triangle(base, height):
    return base*height/2

def rectangle(base, height):
    return base*height

def circle(radius):
    return math.pi*(radius**2)

print(triangle(4,10))

print(os.getcwd)