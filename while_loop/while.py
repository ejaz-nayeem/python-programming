name=input("enter name:")

roll=input("enter your 6 digit roll:")

#print(roll.isdigit())
    
#roll.isdigit()

#if len(roll)==6 and roll.isdigit():
    
 #   print(" valid")
#else:
 #   print("invalid")

while len(roll)!=6 or roll.isdigit()==False:
    if len(roll)!=6:
        print("not valid, please try again")
    
    elif roll.isdigit()==False:
        
        print("not valid, please try again")

    roll=input("enter your 6 digit roll:")
    
    
    
    
print("valid")
