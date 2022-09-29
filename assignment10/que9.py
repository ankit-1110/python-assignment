# Write a python script to print cubes of first N natural numbers.
import math
n=int(input("Enter the value of N:\n"))
for i in range(n):
    p=i+1
    print(int(math.pow(p,3)))