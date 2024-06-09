l1=[1,3,5]
l2=[2,4]
l3=[]
i=0
if len(l1)>=len(l2):
    
    
    
    while i<len(l2):
        
        
    
        l3.append(l1[i])
        l3.append(l2[i])
        i+=1
    for i in range(len(l2),len(l1)):
        l3.append(l1[i])
    
    



    

#l3.extend(l1,l2)    
print(l3)
