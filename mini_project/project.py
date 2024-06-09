name_of_the_year=input("enter the year")
n=int(input("enter number of students:"))
student=0

while student<n:
    
    roll=input("enter your 6 digit roll:")

    while len(roll)!=6 or roll.isdigit()==False:
        
        if len(roll)!=6:
            
            print("not valid, please try again")
    
        elif roll.isdigit()==False:
            
            
        
            print("not valid, please try again")

        roll=input("enter your 6 digit roll:")
    
    
    

    mark=0
    total_mark=0
    subject=0
    while subject<5:
        
    
        subject=subject+1
        
        mark=int(input("enter marks"))
        total_mark=total_mark+mark
    print(" total mark of", roll, "is", total_mark)    
    print(" avg of", roll, "is", total_mark/5)
    student=student+1

record_of_the_students={
    
    name_of_the_year:{
        roll:
        {"total": total_mark, "avg": total_mark/5}
        }
    }
x=input("enter the year name you want to know about: " )
y=input("enter roll of the student: " )
w=input("enter total if you want to know total or enter avg if you want to know average of student: " )
#v=input("enter avg if you want to know average of student: " )


#if y=="roll":
if w=="total":
    
    print("total is", record_of_the_students[x][y][w])
elif w=="avg":
    
    print("average  is", record_of_the_students[x][y][w])
        
    
    
#elif y=="avg":
#    print("avg of ", roll, " is ", record_of_the_students[x][y])
#else:
#    print("we don't have that information")


z=int(input("enter 1 if you want to quit, if not then press any key to continue: " ))
while z!=1:
    
    x=input("enter the year name you want to know about: " )
    y=input("enter roll of the student: " )
    w=input("enter total if you want to know total or enter avg if you want to know average of student: " )
    #y=input("enter what you want to know  about the student: " )

    
        
    if w=="total":
        
            
            
        print("total is", record_of_the_students[x][y][w])
    elif w=="avg":
            
        print("average is", record_of_the_students[x][y][w])
    
    
    z=int(input("enter 1 if you want to quit, if not then press any key to continue: " ))
    
    


