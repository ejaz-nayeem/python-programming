a={11,13,15,18,20}
d=16
l=list(a)
b=[]
for i in l:
    if i<d:
        b.append(i)
actual=max(b)
l.remove(actual)
s=set(l)
print(s)
print(actual)
