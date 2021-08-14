sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
leng = len(sampleList)//3
# print(leng)
start = 0
last = leng

for i in range(1, 4, 1):
    ind = slice(start, last, 1)
    list_part = sampleList[ind]
    print("Part", i, list_part)
    print("After reversing:", list(reversed(list_part)))
    start = last
    if(i != 2):
        last += leng
    else:
        last += len(sampleList) - leng
