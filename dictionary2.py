i1={'pl1':20,'pl3':60,'pl4':32}
i2={'pl1':38,'pl2':52,'pl3':40}
i3={'pl2':35,'pl3':40,'pl4':25}
d={}
for i in i1.keys():
    d[i]=i1[i]
print(d)
for i in i2.keys():
    if i in d.keys():
        d[i]=d[i]+i2[i]
    else:
        d[i]=i2[i]
print(d)
print("Sum of all the players score:")
for i in i3.keys():
    if i in d.keys():
        d[i]=d[i]+i3[i]
    else:
        d[i]=i3[i]
print(d)
