print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.exit")
while True:
    
    choice=int(input("enter your choice:"))
    if choice in(1,2,3,4,5):
        num1=float(input("enter first num:"))
        num2=float(input("enter second num:"))
        if choice ==1:
             print(num1+num2)
        elif choice ==2:
            print(num1-num2)
        elif choice ==3:
            print(num1*num2)
        elif choice ==4:
            print(num1/num2)
    elif choice ==5:
        break
    else:
        print("invalid input")
