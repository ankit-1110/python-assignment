# write a python script to calculate simple interest
a=int(input("enter the principal to calulate simple intrest:\n"))
b=int(input("enter the rate of intrest:\n"))

t=int(input("enter the time period in no.of years:\n"))
si=(a*b*t)/100
print("simple intrest: "+str(si))