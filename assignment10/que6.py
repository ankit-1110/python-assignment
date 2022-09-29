# Write a python script to print first N even natural numbers
n=int(input("Enter the value of N:\n"))
for i in range(n):
    p=i+1
    if(p%2==0):
        print("Even Number "+str(p))