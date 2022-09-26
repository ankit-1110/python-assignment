# Write a python script to display the current date and time.
#  First create variables tostore date and time, 
# then display date and time in proper format (like: 13-8-2022 and9:00 PM)

from datetime import datetime
t=datetime.now()
a=t.strftime("%d-%m-%y,%H %p")
print(a)