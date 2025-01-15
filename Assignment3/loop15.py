'''Q. When interest compounds q times per year at an annual rate of r % for n years, the principle p 
compounds to an amount a as per the following formula. Write a program to read 10 sets of p, r, 
n & t.'''

set=10
while(set>0):
    p=float(input("Enter the principle:"))
    r=float(input("Enter the rate of interest:"))
    n=float(input("Interest compounds how many times per year:"))
    t=float(input("Enter year:"))
    r=r/100
    a = p * ((1 + r / n) ** (n * t))
    print('Amount=',a)
    set=set-1
