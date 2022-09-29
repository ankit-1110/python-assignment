# Write a python script to print first N terms of a Fibonacci series
n=int(input("Enter the number N:\n"))
first=0
second=1
print(first)
print(second)
i=0
while(i<n):
    third=first+second
    print(third)
    first=second
    second= third
    i+=1