A=[]
n=int(input("Enter N for N x N matrix : "))         
print("Enter the element ::>")
for i in range(n): 
   row=[]                                        
for j in range(n): 
   row.append(int(input()))                
A.append(row)                              
print(A)

print("Display Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(A[i][j], end=" ")                  
   print() 
B=[]
n=int(input("Enter N for N x N matrix : "))        

print("Enter the element ::>")
for i in range(n): 
   row=[]                                        
   for j in range(n): 
      row.append(int(input()))            
   B.append(row)                            
print(B)

print("Display Array In Matrix Form")
for i in range(n):
   for j in range(n):
      print(B[i][j], end=" ")
   print()                                            
result = [[0,0,0], [0,0,0], [0,0,0]] 
 
for i in range(n):    
 for j in range(len(A[0])): 
   result[i][j] = A[i][j] + B[i][j] 
print("Resultant Matrix is ::>")
for r in result: 
   print("Resultant Matrix is ::>",r)
