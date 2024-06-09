l1=[1,2,3,3,4]
l2=[3,2,8]
l3=[]
for i in l2:
    for j in l1:
        if i==j:
            l3.append(i)
            l3.sort()
    
print(l3)
