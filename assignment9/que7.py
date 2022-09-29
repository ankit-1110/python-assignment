# rite a python script to print first N even natural numbers in reverse order
a=int(input("Enter the value of N to print N even natural number in reverse order:\n"))
i=0
print()
while(i<2*a):
    print(2*a-i)
    i+=2
print("end")