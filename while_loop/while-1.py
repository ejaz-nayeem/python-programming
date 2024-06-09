#y=int(input("enter hnumber of student"))
x=int(input("enter how many subjects?"))

#for i in range(y):

mark=0
total_mark=0
subject=0
while subject<x:
    
    subject=subject+1
        
    mark=int(input("enter marks"))
    total_mark=total_mark+mark
print(" avg of 1st student is", total_mark/x)

z=int(input("if you want to calculate avg for another then press 1, if not then press any\
              press 0 "))

while z==1:
    mark=0
    total_mark=0
    subject=0
    while subject<x:
        
        subject=subject+1
            
        mark=int(input("enter marks"))
        total_mark=total_mark+mark
    print("your avg is", total_mark/x)
    z=int(input("if you want to calculate avg for another then press 1, \
                 if not then press any press 0 "))
             

    
    


