# print current and previous number and sum
prev = 0
for i in range(10):
    sum = prev + i
    print("Current Number is {0} previous number is {1} & the sum is {2} ".format(i, prev, sum))
    prev = i