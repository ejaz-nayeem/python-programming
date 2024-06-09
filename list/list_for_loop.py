l = [1, 2, 3, 4, 5, 6]
is_ascending = True

for i in range(1, len(l)):
    if l[i] < l[i - 1]:
        is_ascending = False
        break

print(f"Is the list ascending? {is_ascending}")
