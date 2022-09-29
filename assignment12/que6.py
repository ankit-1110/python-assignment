# Write a python script to print first N prime numbers

n=int(input("Enter the number:\n"))
l=0
print()
print(1)
for i in range(2,n*n):
    count=0
    for j  in range(1,i-1):
        p=j+1
        if(i%p==0):
            count=count+1
            
    if(count==0):
        print(i)
        l+=1
    if(l==n-1):
        break