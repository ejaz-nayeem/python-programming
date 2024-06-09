f=open("read.txt", "r")
l=[]
for line in f:
    
    l.append(line)
f.close()
print(l)
