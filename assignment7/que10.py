# Write a program to display day name on the basis of user’s liking of a colour.
#  Askuser for his favorite colour. User can answer in a sentence like “I like red colour”.
#  Assuming all colour name entered by user is in lowercase.
#   Use match case to displayday name associated with the colour.a.Yellow - 
#   Mondayb.Blue - Tuesdayc.Orange - Wednesdayd.White - Thursdaye.Black - Fridayf.Red - Saturdayg.All other colours - Sunday




a=input("Enter the favorite colour:\n")
match a:
    case "yellow":print("Monday")
    case "blue":print("Tuesday")
    case "orange":print("Wednesday")
    case "white":print("Thursday")
    case "black":print("Friday")
    case "red":print("Saturday")
    case _:print("Sunday")