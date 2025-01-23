'''Q.  Given three points (x1, y1), (x2, y2) and (x3, y3), write a program to check if all the three 
points fall on one straight line.'''

x1=int(input("Enter value of x1:"))
y1=int(input("Enter value of y1:"))
x2=int(input("Enter value of x2:"))
y2=int(input("Enter value of y2:"))
x3=int(input("Enter value of x3:"))
y3=int(input("Enter value of y3:"))
m1=(y2-y1)/(x2-x1)
m2=(y3-y1)/(x2-x1)
if m1==m2:
    print("All the points falls on a straight line.")
else:
    print("All the points do not falls on a straight line.")
