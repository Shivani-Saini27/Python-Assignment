def calcSum(x):
    if x:
        return x + calcSum(x-1)
    else:
        return 0

result = calcSum(10)
print(result)