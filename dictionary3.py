words={'A':'Ant','K':'King','B':'Big','S':'Small','G':'Great'}
print(words)
item='Great'
for k in words:
    if words[k]==item:
        words[k]=input("Enter some word:")
print(words)
for i in sorted(words):
    w=dict(sorted(words.items()))
print(w)        

