def getUserInput(message):
    userIn = input(message)
    return(int(userIn))


def fizz_buzz():
    val = getUserInput('Give me an integar ----> ')
    if(val % 5) == 0 and (val % 3) == 0:
        return('FizzBuzz')
    if(val % 3) == 0:
        return('Fizz')
    if(val % 5) == 0:
        return('Buzz')
    else:
        return(val)

print(fizz_buzz())
