# Write a python script to check whether a given number is Prime or not
n=int(input("Enter the number:\n"))
for i in range(2,n//2):
    
    if(n%i==0):
        print("Number is not prime")
        break
    else:
        print("Number is prime")
        break
