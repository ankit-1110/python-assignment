# Write a Python script to create a list of first N natural numbers
a=int(input("Enter the value of N:\n"))
l=[]
i=0
while(i<a):
    l.append(int(input("Enter the value to put in list:")))
    i+=1
print(l)