# Importing Math
# import math
# Program to calculate Area of Triangle
# Formula: [Area of a triangle = (s*(s-a)*(s-b)*(s-c))-1/2]
print("Enter three sides of a triangle")
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
# Calculating Semi-Perimiter
s = (a + b + c) / 2
# Calculating Area using formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# area = math.sqrt((s * (s - a) * (s - b) * (s - c)))
print("THe value of semi-perimeter is : %0.2f" %s)
print("The area of a triangle is : %0.2f" %area)