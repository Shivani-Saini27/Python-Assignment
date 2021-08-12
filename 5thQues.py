n = int(input("Enter number of elements :"))
list1 = []
for i in range(0, n):
    temp = int(input())
 
    list1.append(temp) 

def func():
    n= len(list1)
    if(list1[0] == list1[n-1]):
        print(True)
    else:
        print(False)

func()
