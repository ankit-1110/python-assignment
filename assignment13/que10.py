# Write a Python script to create a list, 
# where each element of the list is a digit of agiven number.


import math
a=int(input("Enter the digit:\n"))
l=[]
b=a
c=0
while(b>1):
    c+=1
    b=b/10
    
print(c)
while(c!=0):
    d=a%math.pow(10,c-1)
    a=a/math.pow(10,c-1)
    
    l.append(int(a))
    a=d
    c-=1

print(l)