# Write a python script to print 
# all Prime numbers between two given numbers (bothvalues inclusive)
n=int(input("Enter the start number:\n"))
m=int(input("Enter the last number:\n"))
for i in range(n,m+1):
    count=0
    for j  in range(1,i-1):
        p=j+1
        if(i%p==0):
            count=count+1
            
    if(count==0):
        print(i)
