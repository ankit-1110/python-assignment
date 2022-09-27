# Write a python script to take the month value in numeric format and display the
# number of days in it.
a=int(input("Enter the month number:\n"))
if(a==1 or a==3 or a==5 or a==8 or a==10 or a==12):
    print("No of days is 31")
elif(a==4 or a==6 or a==7 or a==9 or a==11):
    print("No of day is 30")
elif(a==2):
    print("No of day is 28")
else:
    print("Wrong choice!!")
