# Write a python script to print first M multiples of N
n=int(input("Enter the value of N:\n"))
m=int(input("Enter the value of M:\n"))
for i in range(m):
    p=i+1
    print(n*p)