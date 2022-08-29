n = int(input("Enter the number:"))
rev = 0
original = n
while n != 0:
 last = n % 10
 n = n // 10
 rev = rev*10 + last
if original == rev:
 print("Palindrome Number")
else:
 print("Not a Palindrome Number")
