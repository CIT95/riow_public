import math
# Rio's Code for Week 3 LT


def getUserInput(message):
    try:
        userIn = input(message)
        return(int(userIn))
    except ValueError:
        print('Make sure you enter a numeric value')


def isPrime(val):
    if val > 1:
        stop = (val//2 + 2)

        for n in range(2, stop):
            if (val % n) == 0:
                break
            else:
                if n == val//2 + 1:
                    print(str(val) + ': is a prime number')

run = 'Y'
while run == 'Y':
    
    start = getUserInput('Starting value --> ')
    end = getUserInput('Ending value   --> ')
    try:
        if(start < end):
            for val in range(start, end + 1):
                isPrime(val)
        
    except TypeError:
        print('Input was in error')
    else:
        print('Starting number needs to be less than ending number')
   
    #ask user if they run to run the code again
    print('Run again? Y for yes')
    run = input()

    if(run != 'Y'):
        #if user enter anything but capital Y end the program
        print('Thanks for running my code!')
    continue
