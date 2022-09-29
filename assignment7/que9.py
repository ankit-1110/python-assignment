# Write a python script to check whether a given year isa.Non century leap yearb.
# Century leap yearc.Non century non leap yeard.Century non leap year
a=int(input("Enter the year:\n"))
if(a%100==0):
    if(a%400==0):
        print("leap year")
    else:
        print("Not a leap year")

elif(a%4==0):
    print("leap year")
else:
      print("Not a leap year")