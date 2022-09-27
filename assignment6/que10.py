# Write a python script to print greater among three numbers. Print number only once
# even if the numbers are the same.
a=int(input("Enter the first Number:\n"))
b=int(input("Enter the second Number:\n"))
c=int(input("Enter the third Number:\n"))
if(a>b):
    if(a>c):
        print("First number is largest")
    else:
        print("Third number is largest")
else:
    if(b>c):
        print("second number is largest")
    else:
        print("Third number is largest")

