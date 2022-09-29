# Write a python script to print all Prime numbers under 100
#n=int(input("Enter the number:\n"))


for i in range(2,100):
    count=0
    for j  in range(1,i-1):
        p=j+1
        if(i%p==0):
            count=count+1
            
    if(count==0):
        print(i)
            