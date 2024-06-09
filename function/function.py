def age():
    x=int(input("enter age:"))
    return x
    #print("your age is ", x)
def name():
    y=input("enter name:")
    #print("your name is ", x)
    return y
    
def show_age(function_name1, function_name2):
    x=function_name1()
    #print("age is", x)
    
    y=function_name2()
    z= 2023-x
    print("hello ", y, "your birth year is ", z)

show_age(age, name)
