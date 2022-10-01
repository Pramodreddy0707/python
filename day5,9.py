n= int(input("enter age"))
if(n>0):
    if(n>18):
        print(" allowed")
    else:
        if(n<=18):
           n=18-n
        print("allowed to vote=",n,"years")
else:
    print("not valid")
