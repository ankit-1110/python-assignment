# Write a python script to reverse a number.
import math
n=int(input("Enter the number:\n"))
a=n
count=1
sum=0
if n>9:
    for i in range(n):
        if a>9:
            count=count+1
            a=a//10
print(count)
for i in range(count):
    p=i+1
    d1=n%10
    sum=sum+d1*int(math.pow(10,count-p))
    n=n//10
print(sum)    