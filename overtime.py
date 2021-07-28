#Ferrer, Marion Caryl R.
#ELE2C 3ITD
#Feb. 19, 2021
#Lab Activity 1


import math
import sys

def overtime():
    try:
        workHours = float(input('Enter the employee\'s work hours for the week: '))
        hourRate = float(input('Enter the employee\'s regular hourly rate: '))

        if workHours > 40.0:
            totalSal = 40.0 * hourRate + 2 * hourRate * (workHours - 40.0)
            print(f'Your total wage for the week is: ', round(totalSal,2))
        else:
            totalSal = workHours * hourRate
            print(f'Your total wage for the week is: ', round(totalSal,2))

    except:
        print('Invalid value entered!')


#Start program from here
overtime()

while True:
    tryAgain= input('Try again (Y/N): ')

    if tryAgain == 'Y':
        overtime()
    elif tryAgain == 'N':
        print('Thank you...')
        sys.exit()   #just like s.close(); in Java
    else:
        tryAgain     #for invalid inputs ?
