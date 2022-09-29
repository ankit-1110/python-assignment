# Write a python program to check whether a given string is a multiword string or single
# word string using match case statement
a=input("Enter the string:\n")
b=a.count(" ")
c=b>0

match(c):
    case True: print("Multiword")
    case False: print("Single string")
    