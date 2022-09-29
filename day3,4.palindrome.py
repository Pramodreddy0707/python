firstList =  [] 

n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    firstlist.append(ele)  
print(firstlist)

secondList =  [] 

n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    secondlist.append(ele)  
print(secondlist)

result = []
i, j = 0,0
while i < len(firstList) and j < len(secondList):
    if firstList[i] < secondList[j]:
      result.append(firstList[i])
      i = i+1
    else:
      result.append(secondList[j])
      j = j+1

result = result + firstList[i:] + secondList[j:]
print ("Sorted List: " + str(result))
