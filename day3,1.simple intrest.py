p=int(input("Enter the principle :"))
t=int(input("Enter the time :"))
age=int(input("Enter your age:"))

if age<50:
    r=12
    i=p*t*r/100
    print("simple Intreset:",i)
elif age>50:
    r=10
    i=p*t*r/100
    print("simple Intreset:",i)
else:
    print("enter name is invalid")
    
