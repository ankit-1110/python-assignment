# Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part
print("Enter the value of complex number a+ib:\n")
a=int(input("Enter the value of a:\n"))
b=int(input("Enter the value of b:\n"))
if(a>b):
    print("Real part is greater")
else:
    print("Imaginary part is greater")

