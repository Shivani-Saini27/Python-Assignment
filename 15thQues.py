list_ = [11, 45, 8, 11, 23, 45, 23, 45, 89]
count = 0

dictionary = dict()
for i in list_:
    if(i in dictionary):
        dictionary[i] += 1
    else:
        dictionary[i] = 1
        
print(dictionary)