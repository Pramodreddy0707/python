num=int(input("enter a number: "))
reversed_num=0
while num!=0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num//=10
    print("reversed_num: "+str(reversed_num))
