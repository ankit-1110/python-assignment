# Write a python script to print table of user’s choice
n=int(input("Enter the value of N to print table:\n"))
for i in range(10):
    p=i+1
    print(str(n)+"*"+str(p)+"="+str(n*p))