'''Q. Two numbers are input through the keyboard into two locations C and D. Write a program
to interchange the contents of C and D.'''

A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
print("Before interchange: A=",A, "and B=",B)
temp=A
A=B
B=temp
print("After interchange: A=",A, "and B=",B)
