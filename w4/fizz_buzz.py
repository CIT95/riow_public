def getUserInput(message):
    try:
        userIn = input(message)
        return(int(userIn))
    except ValueError:
        print('Make sure you enter a numeric value')


def fizz_buzz():

    val = getUserInput('Give me an integar ----> ')
    try:
        if(val % 5) == 0 and (val % 3) == 0:
            return('FizzBuzz')
        if(val % 3) == 0:
            return('Fizz')
        if(val % 5) == 0:
            return('Buzz')
    except TypeError:
        print('User Input in error')        
    else:
        return(val)


print(fizz_buzz())
