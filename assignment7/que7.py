# Write a python program to check whether a given number is positive, negative or
# zero using match case statement
a=int(input("Enter the number:\n"))
match a>0:
    case True: print("Positive")
    case False: print("zero") if(a==0) else print("Negative")
    
