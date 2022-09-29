# Write a Python script to create a list of first N even natural numbers
a=int(input("Enter the value of N:\n"))
l=[]
i=1
while(i<=2*a):
    if(i%2==0):
        l.append(int(i))
    i+=1

print(l)