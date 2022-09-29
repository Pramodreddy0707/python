firstList = [2,7,8,9] 
secondList =[0,1,4,6]
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
 
