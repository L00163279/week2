# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................
#Read 5 book titles and book cost
#check running total by using while loop
#print total running cost

number = 0
running_total = 0
while 1:
    if number < 5:
        booktitle = input("enter book title ")
        bookvalue = float(input("enter book value "))
        running_total = running_total + bookvalue
        #print("{}".format(running_total))
        number=number+1
    else:
        break

print("Total Running Total is {}".format(running_total))

