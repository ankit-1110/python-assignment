# Write a python script to calculate sum of squares of first N natural numbers
n=int(input("Enter the value of N:\n"))
sum=0
for i in range(n):
    p=i+1
    sum=sum+p*p
print(sum) 