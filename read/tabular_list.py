f=open("1.txt")
#f.split()

l=[]
for line in f:
    l.append([int(n) for n in line.split()])

f.close()
print(l)
    
