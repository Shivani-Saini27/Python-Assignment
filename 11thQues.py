str = "PyNaTive"
lower = []
upper = []
for char in str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_string = ''.join(lower + upper)
print(sorted_string)