d={"sonam":1,"subham":2,3:[10,20,30],4:{5:'a',6:'b'}}
print(d["sonam"])
print(d[3])
print(d[4])
print(d[3][0])
print(d[4][5])
print(d.items())
print(d.keys())
print(d.values())
d[3]='Abhay'
print(d)
d[5]='Puja'
print(d)
e=dict(name='abc',roll=13)
print(e)
r=[1,2,3,4,5,6]
n=['a','b','c','d','e','f']
f=dict(zip(r,n))
print(f)
'''for i in f.keys():
    print(i)
for i in f.values():
    print(i)
for i in f.items():
    print(i)    
score={'pl1':100,'pl2':80,'pl3':72,'pl4':85,'pl5':130,'pl6':102}
sum=0
max=0
for i in score.values():
    sum=sum+i
    if i>max:
        max=i
print("sum=",sum)'''



