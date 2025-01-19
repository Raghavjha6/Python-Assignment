score={'pl1':100,'pl2':80,'pl3':72,'pl4':85,'pl5':130,'pl6':102}
for i in score.keys():
    if max not in score.keys():
        max=i
    else:
        if score[i]>score[max]:
            max=i
print("max scorer player=",max)
