s=("a","b")
d={"a":1,"b":3,"c":4,"d":6}
t=0
item=0
for i in s:
    t=t+d[i]
    item+=1
    if t>=5:
        break
print(item)
    
