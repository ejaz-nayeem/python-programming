a=[1,2,3,4]
b={1:9,3:90,5:78}
s=[]
for i in b:
    for j in a:
        if i==j:
            s.append(j)
    

print(set(a))
print(s)
e=[]
for i in a:
    if i not in s:
        e.append(i)
e=set(e)        
print(e)
