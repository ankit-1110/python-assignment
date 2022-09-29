# Write a python script to check whether two given strings are identical, 
# first stringcomes before the second in dictionary order or first string 
# comes after the secondstring in dictionary order using match case statement
first="List"
second="String"


match first>second:
    case True:print("First string comes after the second")
    case False: print("identical") if(first==second) else print("first string comes before the second")