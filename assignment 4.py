num=int(input("enter a number"))
if num<=0:
    print("Enter a positive number")
else:
    print("multiplication table of",num)
    for i in range(1,11):
        print(num,"x",i,"=",num * i)
