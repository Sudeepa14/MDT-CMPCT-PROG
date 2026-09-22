# Task 1 - circle area calculator
from math import pi

if __name__ == '__main__':
    r = float(input("Input the radius of the circle : "))

    # area of a circle = pi * r^2
    area = pi * r ** 2

    print("The area of the circle with radius " + str(r) + " is: " + str(area))
