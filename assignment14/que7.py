# Write a Python script to remove all non int values from a list
l1=[1,2,3,'s','d',True]
l2=[]
for i in l1:
    if(type(i)==int):
        l2.append(i)
l1=l2
print(l2)

