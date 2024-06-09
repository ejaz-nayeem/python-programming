def find(word, letter, index):
    #index=0
    while index<len(word):
        
        if word[index]==letter:
            #return index
            print(index)
        index=index+1
    #print(index)
    return -1

find("ejaz", 'z', 0)
