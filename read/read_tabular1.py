f=open("read_tabular2.txt")
l=[]

for line in f:
    l.append([int(n) for n in line.split()])
    

    


f.close()
print(l)
