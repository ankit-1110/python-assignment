# Write a Python script to create a list of first N odd natural number
a=int(input("Enter the value of N:\n"))
l=[]
i=1
while(i<2*a):
    if(i%2!=0):
        l.append(i)
    i+=1

print(l)