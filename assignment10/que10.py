# Write a python script to display all prime numbers within a range.# rangestart = 15end = 45
#n=int(input("Enter the value of N:\n"))

for i in range(15,45):
    count=0
    for j in range(2,int(i/2)):
                    if(i%j==0):
                            count+=1
    if(count==0):
        print(i)                        
                    




            







       


  
