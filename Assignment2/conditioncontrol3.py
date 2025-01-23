'''Q. Any year is input through the keyboard. Write a program to determine whether the year is a 
leap year or not.'''

year=int(input("Enter the year:"))
if(year%400==0)or(year%100!=0)and(year%4==0):
    print(year,"is a leap year")
else:
    print(year,"is not leap year")
