# Write a Python script to create a list of city names taken from the user.

n=int(input("enter how many city you want to add: "))
l=[]
i=0
while(i<n):
    l.append(input("Enter the city name: "))
    i+=1

print(l)