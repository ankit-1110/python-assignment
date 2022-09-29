# Write a program which takes a number from user. Print Saurabh Shukla if the number
# is even, print Prateek Jain if the number is negative odd number and print Aditya
# Choudhary if number is positive odd number.
num=int(input("Enter the number:\n"))
if(num>0):
    if(num%2==0):
        print("Saurabh shukla")
    else:
        print("Aditya choudhary")
else:
    if(num%2==0):
        print("Saurabh shukla")
    else:
        print("Prateek jain")