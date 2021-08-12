# question 6

n = int(input("Enter number of elements :"))
list2 = []
for i in range(0, n):
    temp = int(input())
 
    list2.append(temp) 

def fun():
    for i in range(len(list2)):
        if(list2[i]%5 == 0):
            print(list2[i])
        
fun()



# question 7
string = "Emma is good developer. Emma is a writer"
print(string.count("Emma"))



# question 8
ori_num = input("Enter the no:")
rev_num = ori_num[::-1]

if(ori_num == rev_num):
    print("Original and revrese number are same")
else:
    print("Original and reverse number are not same")

