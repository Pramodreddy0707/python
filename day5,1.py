A=int(input('Enter A: '))
B=int(input('Enter B: '))
if A>B:
    print("please enter small input in A than B")
for number in range(A,B+1):
    factor=0
    for i in range(1,number):
      if number%i==0:
        factor=i
    if factor>1:
      print (number)
