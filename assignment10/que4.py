# Write a python script to print the first 10 multiples of N in reverse order.
n=int(input("Enter the value of N:\n"))
for i in range(10):
    p=i+1
    print(n*(11-p))