'''Q. If the three sides of a triangle are entered through the keyboard, write a program to check 
whether the triangle is isosceles, equilateral, scalene or right angled triangle.'''

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))
if a+b>c and b+c>a and c+a>b:
    if a == b == c:
        print("The triangle is an equilateral triangle.")
    elif a != b and b != c and c != a:
        print("The triangle is a scalene triangle.")
    else:
        print("The triangle is an isosceles triangle.")
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("The triangle is right-angled triangle.")
else:
    print("The entered side do not form a valid triangle.")
