# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date: 30/09/2021
# Modified Date: 
# Description :
# Listening : Muhammed Shafeeq Thottathil, LYIT

# ...............................





ActualNo=6
while 1:
    print("guess a number from 1 -10")
    GuessNo=int(input())
    if GuessNo == ActualNo:
        print("Yes, The Number is correct. Its ".format(ActualNo))
        break
    elif GuessNo != ActualNo:
        print("Not correct..Do you wish to retry. Y/N")
        retry=input()
        if retry == 'N':
            break
