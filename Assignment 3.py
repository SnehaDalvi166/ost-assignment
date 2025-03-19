num=int(input("enter a number"))
i=1
sum=0
if num<=0:
    print("enter a positive number")
else:
    print("the numbers are")
    while(i<=num):
        print(i)
        sum=sum+i
        i=i+1
    print("The sum is",sum)
