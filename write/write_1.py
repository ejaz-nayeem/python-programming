l=[1 ,2, 3]
k=",".join(str(x) for x in l)
#k=[str(x) for x in l]

    

f=open("write1.txt", "w")



f.write(k)


f.close()
