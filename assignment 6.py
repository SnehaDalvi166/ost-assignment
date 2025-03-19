def sequential_search(list1,n,key):
    #searching list1 sequentially
    for i in range(0,n):
        if(list1[i] == key):
            return i
    return -1

#create a list of numbers
n = int(input("enter size of n"))
list1=[]
print("enter",n,"elements")
for i in range(0,n):
    list1.append(int(input()))
    
print("given list is",list1)
key = int(input("enter an element you wish to search from a list:"))
n = len(list1)
#call funvtion sequential search
res=sequential_search(list1,n,key)
if(res == -1):
    print("element not found")
else:
    print("element found at index:",res)
