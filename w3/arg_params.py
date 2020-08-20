def timeToCharge(kWh, percentFull):
    return kWh * (1 - percentFull)

def determineNextSteps(time):
    if(time > 12):
        print('need more kWh')
    else:
        print('that will work') 

chargeTime = timeToCharge(200, .80)
print(chargeTime)
determineNextSteps(chargeTime)

chargeTime = timeToCharge(10, .50)
print(chargeTime)
determineNextSteps(chargeTime)




""" def checkInput(user, message):
    if(user == '' or message == ''):
        greeting()
    else:
        greeting(user, message)    
    

def greeting(user='Who Dis?', message='No Message?' ): 
    print('Hello ' + user + 'nice to hear you say ' + message)
    

user = input('Username') 
message = input('Message') 

result = checkInput(user, message)
 """



""" def getUserInput(message):
    return(input(message))

def greeting(user='Who Dis?', age=3):
    print('UserName ' + user + ' your age is ' + str(age))

user = getUserInput('Who Dis? --->')
age = getUserInput('Your Age? --->')

greeting()
greeting(user, age)
greeting('Rio')
greeting(age = 9) """
