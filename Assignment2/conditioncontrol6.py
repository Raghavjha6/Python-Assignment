'''Q.  If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to 
determine the youngest of the three.'''

ram=int(input("Enter the age of Ram:"))
shyam=int(input("Enter the age of shyam:"))
ajay=int(input("Enter the age of ajay:"))
if(ram<shyam)and(ram<ajay):
    print("Ram is youngest of three")
elif(shyam<ram)and(shyam<ajay):
    print("Shyam is youngest of three")    
else:
    print("Ajay is youngest of three")  
