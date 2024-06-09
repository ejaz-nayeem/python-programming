tem=[
   [1234, 4, 5, 6],
   [6543, 8, 9, 0],
   [2345, 5, 6, 34]


    ]
f=open("5.txt", "w")
for line in tem:
    f.write(",".join([str(i) for i in line])+"\n")

f.close()
