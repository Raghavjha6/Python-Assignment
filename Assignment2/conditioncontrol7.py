'''Q. Write a program to check whether a triangle is valid or not, when the three angles of the 
triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles 
is equal to 180 degrees.'''

ang1=float(input("Enter the value of angle 1:"))
ang2=float(input("Enter the value of angle 2:"))
ang3=float(input("Enter the value of angle 3:"))
if(ang1+ang2+ang3==180):
    print("It is a valid triangle.")
else:
    print("It is not valid triangle.")  
