# Write a menu driven program to perform following operations -
#  Addition, Subtraction,
# Multiplication, Division
num =int(input("Select option\nAddition:Press 1\nSubtraction:Press 2\nMultiplication:Press 3\ndivision:Press 4\n"))
match(num):
    case(1):
            num1=int(input("Enter the first number:\n"))
            num2=int(input("Enter the first number:\n"))
            sum=num1+num2
            print("Sum is:"+str(sum))
    case(2):
            num1=int(input("Enter the first number:\n"))
            num2=int(input("Enter the first number:\n"))
            sub=num1-num2
            print("Sum is:"+str(sub))
    case(3):
            num1=int(input("Enter the first number:\n"))
            num2=int(input("Enter the first number:\n"))
            mul=num1*num2
            print("Sum is:"+str(mul))
    case(4):
            num1=int(input("Enter the first number:\n"))
            num2=int(input("Enter the first number:\n"))
            div=num1/num2
            print("Sum is:"+str(div))                        
    case _: print("Wrong choice!!!")