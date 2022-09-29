# Write a python script to calculate sum of cubes of first N natural numbers
import math


n=int(input("Enter the value of N:\n"))
sum=0
for i in range(n):
    p=i+1
    sum=sum+int(math.pow(p,3))
print(sum)