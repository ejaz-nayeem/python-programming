l=[
    [2, 3, 4],
    [2,55,66],
    [55, 666,555]
    ]
#k=",".join(str(x) for x in l)
#print(k)

#for i in k:
#    print(k[i]+"\n")
#print(k)
f=open("write2.txt", "w")
for line in l:
    f.write((",".join(str(x) for x in line))+"\n")

#f.write(i+"\n" for i in k)
f.close()
