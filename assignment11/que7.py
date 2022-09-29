# Write a python script to count digits in a given number
n=int(input("Enter the number:\n"))
count=1
if(n>9):
    for i in range(n):
        if(n>9):
            count=count+1
            n=n//10
print("Number of digits: "+str(count))            
