'''Q. Given the coordinates (x, y) of a center of a circle and it’s radius, write a program which will 
determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use 
sqrt( ) and pow( ) functions).'''

import math
x, y = map(int, input("Enter point coordinates (x y): ").split())
r = float(input("Enter circle radius: "))
d=math.sqrt(math.pow(x,2) + math.pow(y,2))
if (r > d):
    print("\n\nThe pints lie inside the circle.");
elif (r == d):
    print("The points lie on the circle.");
else:
    print("The points lie outside the circle.");

