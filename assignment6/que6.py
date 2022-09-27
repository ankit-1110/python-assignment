
# 6. Write a python script to check whether a given number is a three digit number or not.
a=int(input("Enter the three digit number:\n"))
b=a/100
if((b>1 or a==100) and a<=999):
    print("Number is 3 digit")
else:
    print("number is not three digit")
   