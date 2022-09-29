# Write a python script to calculate HCF of two numbers
n1=int(input("Enter the first number:\n"))
n2=int(input("Enter the first number:\n"))
a=n1
b=n2
r=1

while(r!=0):
    r=n1%n2
    n1=n2
    n2=r
print("Hcf is: "+str(n1))
lcm=int((a*b)/n1)
print("Lcm is: "+str(lcm))