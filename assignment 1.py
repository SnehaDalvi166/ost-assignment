n=int(input("enter the number:"))
c=0
a=0
b=1
if n==0 or n==1:
    print("yes it belongs to fibonacci sequence")
elif n<0:
    print("no it does not belongs to fibonacci sequence")
    print("enter a positive input")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("yes it belongs to fibonacci sequence")
    else:
        print("no it does not belongs to fibonacci sequence")

