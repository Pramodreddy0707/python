sub1=int(input("enter the marks: "))
sub2=int(input("enter the marks: "))
sub3=int(input("enter the marks: "))
sub4=int(input("enter the marks: "))
sub5=int(input("enter the marks: "))
total=sub1+sub2+sub3+sub4+sub5
avg=total/5
if avg>91 and avg<=100:
    print("grade is A")
elif avg>81 and avg<=90:
    print("grade is B")
elif avg>71 and avg<=80:
    print("grade is C")
elif avg>61 and avg<=70:
    print("grade is D")
elif avg>51 and avg<=60:
    print("grade is E")
elif avg>0 and avg<=50:
    print("grade is F")
else:
    print("invalid input")
