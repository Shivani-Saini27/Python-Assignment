firstSet = {65, 42, 78, 83, 23, 57, 29}
secondSet = {67, 73, 43, 48, 83, 57, 29}

print("first set:",firstSet)
print("second set:", secondSet)

inters = firstSet.intersection(secondSet)
print(inters)

for i in inters:
    firstSet.remove(i)
    
print("after removing common element:", firstSet)