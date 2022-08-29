import math
n = int(input("Enter the factorial value"))
if n<0:
 print("No Factorial")
else:
 fact = 1
 for i in range(1, n+1):
  fact = fact * i
  print(n,'! =',fact)
  print("factorial():", math.factorial(n))
