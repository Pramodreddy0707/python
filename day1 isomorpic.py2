def isisomorphic(s,t):
     if len(s) != len(t):
         return False
     else:
            d1,d2={},{}
            for i in range (len(s)):
                a,b=s[i],t[i]
                if(a not in d1):
                    d1[a]=b
                if(b not in d2):
                    d2[b]=a
                if d1[a] !=b or d2[b] !=a:    
                 return False
            return True 
s=input("enter the string -")
t=input("enter the string -")
print(isisomorphic(s,t))
 
