# Write a python script to calculate sum of digits of a given number
n=int(input("Enter the number:\n"))
count=1
sum=0

if(n>9):
    for i in range(n):
        if(n>0):
            d1=n%10
            sum=sum+d1
            n=n//10
    print("Sum:"+str(sum))    
else: 
     print("Sum "+str(n))