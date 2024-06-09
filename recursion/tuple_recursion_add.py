def s(t):
    if len(t) == 0:
        return 0
    else:
        return t[0] + s(t[1:])

t = (1, 2, 3, 4, 5, 6)
print(s(t))
