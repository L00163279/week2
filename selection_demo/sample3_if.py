# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:a
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................
if __name__ == '__main__':
        grade = input("enter a grade")
        #print("\n")
        grade = int(grade)
        #print(grade)

        module = "Python"

        if (grade >= 70) and module == "Python":
                print("you have a distinction!!!")

        elif grade >= 60:
                print("You have earned a M.1.")
        elif grade >= 50:
                print("You have earned a M.2.")
        elif grade >= 40:
                print('You have passed')
        else:
                print("Please try again")