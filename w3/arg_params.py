def getUserInput(message):
    return(input(message))

def greeting(user='Who Dis?', age=3):
    print('UserName ' + user + ' your age is ' + str(age))

user = getUserInput('Who Dis? --->')
age = getUserInput('Your Age? --->')

greeting()
greeting(user, age)
greeting('Rio')
