r=int(input("Enter the range:"))
zero_count=0
pos_count=0
neg_count=0
print("Enter the numbers:")
for i in range(r):
    num=int(input())
    if num>0:
        pos_count+=1
    elif num<0:
        neg_count+=1
    else:
        zero_count+=1
print('Positive number count=',pos_count)
print('Negative number count=',neg_count)
print('Zero count=',zero_count)
