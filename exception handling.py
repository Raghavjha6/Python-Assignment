def find (st,ind):
    return st[ind]
st=input('Enter your string:')
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
try:
    print(find(st,5))
except IndexError:
    print('Index error caught.')
try:
    div=a/b
    print(div)
except ZeroDivisionError:
    print('Zero division error occured.')
else:
    print("Exception not occured.")
finally:
    print("Must execute.")
print('End of the program.')
