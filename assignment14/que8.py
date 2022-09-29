# Write a Python script to print distinct elements along with their frequencies of occurrence in the list
l1=[1,4,6,78,90,45,1,6,78]
l2=[]
l3=[]
c=0
for i in l1:
    
    if i not in l2:
        l2.append(i)
    else:
        print("Frequency:"+str(i)+" "+str(l1.count(i)))
        l3.append(i)
print(l1)       #original list
print(l2)       #list without duplicate items
print(l3)       #duplicate item list