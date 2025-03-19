print("--MENU--")
print("1.string swalpcase")
print("2.string length")
print("3.string uppercase")
print("4.string lowercase")
print("5.string indexing")
print("6.string slicing")
print("7.exit")
while True:
    i=int(input("enter your choice"))
    if i==1:
        s1=input("enter string")
        print("String swapcase",s1.swapcase())
    elif i==2:
        s1=input("enter string to find in length")
        print("length of string is",len(s1))
    elif i==3:
        s1=input("enter string in lowercase")
        print("uppercase string",s1.upper())
    elif i==4:
        s1=input("enter string in uppercase")
        print("lowercase string",s1.lower())
    elif i==5:
        s1=input("enter for indexing")
        pos=int(input("enter posotion to extract"))
        print("character at position",pos,"is",s1[pos])
    elif i==6:
        s1=input("enter string for slicing")
        start = int(input("enter starting position to extract"))
        end = int(input("enter ending position to extract"))
        print("Sliced string is",s1[start:end])
    elif i==7:
        break
    else:
        print("invalid choice")
