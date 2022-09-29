# Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.
num=int(input("Enter your choice:\n1Isoceles Traingle:Press 1\nEquilateral Traingle:Press 2\nRight angle Traingle:Press 3\n"))
match(num):
    case 1:
            s1=int(input("Enter the first side of traingle\n"))
            s2=int(input("Enter the Second side of traingle\n"))
            s3=int(input("Enter the third side of traingle\n"))
            if(s1==s2 or s1==s3):
                        if(s1==s3):
                                if(s2==s3):
                                    print("Not an Isoceles trainglle")
                                else:
                                    print("Isoceles traingle")
                        if(s1==s2):
                                if(s2==s3):
                                    print("Not an Isoceles trainglle")
                                else:
                                    print("Isoceles traingle")
            else:
                print(" Not an Isoceles traingle")

    case 2:
            s1=int(input("Enter the first side of traingle\n"))
            s2=int(input("Enter the Second side of traingle\n"))
            s3=int(input("Enter the third side of traingle\n"))
            if(s1==s2 and s1==s3 and s2==s3):
                print("Equilateral traingle")
            else:
                print("Not equilateral traingle")
    case 3:
            s1=int(input("Enter the first side of traingle\n"))
            s2=int(input("Enter the Second side of traingle\n"))
            s3=int(input("Enter the third side of traingle\n"))
            if(((s1**2)==s2**2+s3**2) or ((s2**2)==s1**2+s3**2) or ((s3**2)==s1**2+s2**2)):
                print("Right angle traingle")
            else:
                print("Not a right angle traingle")
    case _: print("Wrong Choice!!!")
2


