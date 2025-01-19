'''Q. The length & breadth of a rectangle and radius of a circle are input through the keyboard.
Write a program to calculate the area & perimeter of the rectangle, and the area &
circumference of the circle.'''

import math
length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))
radius = float(input("Enter radius of the circle: "))
area_rectangle = length * breadth
perimeter_rectangle = 2 * (length + breadth)
area_circle = math.pi * radius ** 2
circumference_circle = 2 * math.pi * radius
print("Area of rectangle:",area_rectangle)
print("Perimeter of rectangle:",perimeter_rectangle)
print("Area of circle:",area_circle)
print("Circumference of circle:",circumference_circle)
