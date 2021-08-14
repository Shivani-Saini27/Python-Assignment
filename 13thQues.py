originalList = [34, 54, 67, 89, 11, 43, 94]

ele = originalList.pop(4)
print("List after removing ele at index 4:", originalList)

originalList.insert(2, ele)
print("List after inserting element at index 2:", originalList)

originalList.append(ele)
print("List after appending element in last:", originalList)