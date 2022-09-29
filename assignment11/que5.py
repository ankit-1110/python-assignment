# Write a python script to calculate sum of first N even natural numbers
n=int(input("Enter the value of N:\n"))
sum=0
for i in range(n):
    p=i+1
    if(p%2==0):
        sum=sum+p
print(sum) 