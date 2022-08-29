no1=int(input("enter the 1st number: "))
no2=int(input("enter the 2nd number:"))
no3=int(input("enter the 3rd number:"))
if (no1>=no2) and (no1>=no3):
    largest=no1

elif(no2>=no1) and (no2>=no3):
    largest=no2
else:
    largest=no3
print("largest number is:", largest)
    
