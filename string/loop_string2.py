s1 = "asddf"
has_dups = False

for i in range(len(s1) - 1):
    if s1[i] == s1[i + 1]:
        has_dups = True
        break

print(has_dups)
