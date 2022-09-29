year=int(input("Enter the year"))
if year%4==0:
    print("given year is an leap year")
elif year<0 or year ==0 :
    print("******INVALID INPUT*****")
else:
    print("given year is not a leap year")
