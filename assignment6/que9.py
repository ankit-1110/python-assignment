# Write a python script to check whether a given year is a leap year or not.
a=int(input("Enter the year:\n"))
if(a%100==0):
            if(a%400==0):
                print("Year is leap year")

            else:
                print("Year is not leap year")
else:
    if(a%4==0):
        print("Year is leap year")
    else:
        print("Year is not leap year")
