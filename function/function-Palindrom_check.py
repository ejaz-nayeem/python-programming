def func(word):
    

    w="" 
    n=-1
    #word=word2
    while n>=-(len(word)):
        w=w+word[n]
        print(word[n])
        n=n-1
    print(w)
    if word==w:
        print(True)
    else:
        print(False)
func("spa")
