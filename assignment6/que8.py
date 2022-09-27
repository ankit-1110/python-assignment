#  Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots
print("Enter the value of quadratic equation ax2+bx+c:\n")
a=int(input("enter the value of a:\n"))
b=int(input("enter the value of b:\n"))
c=int(input("enter the value of c:\n"))
d=b**2-(4*a*c)
if(d>0):
    print("real roots")
elif(d<0):
    print("complex roots")
else:
    print("only one real roots")