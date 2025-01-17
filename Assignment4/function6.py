'''Q. Write a program in Python to print sum of all +ve numbers and all -ve numbers.'''

def sum(r):
    print("Enter the numbers:")
    i=1
    sum=0
    while i<=r:
        num=int(input())
        sum = sum+num
        i=i+1
    return sum
r= int(input("Enter range:"))
s=sum(r)
print("Sum:",s)
