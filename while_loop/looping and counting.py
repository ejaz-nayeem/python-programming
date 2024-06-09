
def count(word, letter_to_count):
    #letter=0
    

    count=0
    for letter in word:
        
        if letter==letter_to_count:
            
            
            count=count+1
    print(count)

count("rebellion", "l")
    
