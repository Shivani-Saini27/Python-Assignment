dictionary = {'John':47, 'Emma':69, 'Kelly':76, 'Jason':97}
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]

rollNumber = [i for i in rollNumber if i in dictionary.values()]
# for i in rollNumber:
#     if not i in dictionary.values():
#         rollNumber.remove(i)
        
print(rollNumber)
