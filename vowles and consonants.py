word = input("Enter the word")
vow = con = 0
for ch in word:
 if ch.lower() in 'aeiou':
     vow = vow + 1
 else:
     con = con + 1
else:
    print("Vowels:", vow)
    print("Consonents:", con)
