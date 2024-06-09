 #(Given the name of the item (a string) we will calculate its power by adding
 #the ASCII code value of each of its characters. you can get the ASCII
 #value of a character using the ord function and passing the character as an argument.
 #Our program will continuously iterate in a sentinel loop allowing the user to choose among four
 #different commands:
 #• "add"- adds a new item. The program will ask for the name, calculate the item’s power and
 #add it to the list.
 #• "print"- prints the current list of magic items and their powers.
 #• "remove"- remove an existing item. The program will ask for the item’s name and remove it
 #from the list (should avoid an error if the item is not in the list).
 #• "quit"- ends the program.)

 #




print("enter the name:")
d=input()
s=[ord(i) for i in d]
#print(s)
i=0
sum=0
list=[(d, sum)]
while i<len(s):
    sum=sum+s[i]
    i=i+1
list=[(d, sum)]
#print(sum)

print(list)

print("if you want another to add type 1, remove then -1, else then terminate ") 
i=int(input())
if i==1:

    
    print("enter the name:")
    d=input()
    s=[ord(i) for i in d]
    print(s)
    i=0
    #sum=0
    #list=[(d, sum)]
    while i<len(s):
        
        
        sum=sum+s[i]
        i=i+1

    list.extend([(d, sum)])
    print(list)
elif i==-1:
    print("enter the name:")
    d=input()
    s=[ord(i) for i in d]
    while i<len(s):
        
        
        sum=sum+s[i]
        i=i+1
    list.remove([(d, sum)])
    print(list)
else:
    print("bye")
    



