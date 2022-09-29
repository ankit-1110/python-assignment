# Write a python script to print binary equivalent of a given decimal number. (do notuse bin() method

n=int(input("Enter the number:\n"))


for i in range(n):
    if(n>=1):
        s= print(n%2,end=" ")
        n=n//2
print(s)





