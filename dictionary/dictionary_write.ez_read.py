f=open("dictionary_write.ez", "r")
list=[]
for line in f:
    list.append(line.rstrip())
f.close()
