# 10.Write a python script to print first 10 multiples of N\
a=int(input("Enter the value of N to print  its multiples:\n"))
i=1
print()
while(i<=10):
    print(str(a)+"*"+str(i)+"="+str(i*a))
    i+=1
print("end")