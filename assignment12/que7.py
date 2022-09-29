# Write a python script to check whether a given pair of numbers are co-Primenumbers or not.
n=int(input("Enter the number:\n"))
m=int(input("Enter the number:\n"))
count=0

for i in range(2,n):
    
    if(n%i==0):
        # print("Number is not prime")
      
        break
    else:
        count+=1
        break
for i in range(2,m):
    
    if(m%i==0):
        # print("Number is not prime")
        break
    else:
        count+=1
        break
if(count==2):
    print("Number is co-prime")
else:
    print("Not co-prime")