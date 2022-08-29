num=input("enter the value=")
if(num.isnumeric()):
    fact=1
    for i in range(1,int(num)+1):
        fact=fact*i
    print("factorial is",fact)
else:
    print("invalid input")
