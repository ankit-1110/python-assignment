# Write a python script to check if a string contains only numbers.
a="string123jing"
c=a.isalpha() #to  check only alphabet
d=a.isdigit() #to check only digit
e=a.isalnum() #to check string conatains both number and alphabets
print(c)
print(d)
print(e)
if(c==True):
    {
        print("Strings only")
    }
else:
    print("Number present")