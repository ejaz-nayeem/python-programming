fib=[0,1]
i=1

while i<=10:
    fib.append(i)
    i=fib[-1]+fib[-2]
    
if 2 in fib:
    fib=fib[fib.index(2):len(fib)]
    
    
    
    
    

print(fib)   
#print(fib2)
