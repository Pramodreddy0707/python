rows=int(input("enter the bumber of rows"))
for i in range(1,rows):
    for j in range (1,rows-i-1):
        print(end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    print()
