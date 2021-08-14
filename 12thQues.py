list1 = [3,6,9,12,15,18,21]
list2 = [4,8,12,16,20,24,28]

odd_list = []
even_list = []

for i in range(len(list1)):
    if i%2 != 0:
        odd_list.append(list1[i])
# print(odd_list)    output: 6, 12, 18
for i in range(len(list2)):
    if i%2 == 0:
        even_list.append(list2[i])

odd_list.extend(even_list)
print(odd_list)