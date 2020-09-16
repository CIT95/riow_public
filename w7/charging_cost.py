#Week 7 Learn Together Code
#My code is modeling the concept of charging my electric car

#DD
from collections import Counter

homeCharging = {
    'kwhUsed': 20,
    'startTime': '1am',
    'endTime': '5am',
    'cost': 6
}

#add a key to a dd
print(homeCharging.setdefault('peak', False))

#check whether a given key already exists in a dd
print(homeCharging.get('kwhUsed', 0))
print(homeCharging)

#iterate over dd using for loops
for session, values in homeCharging.items():
    print(session, values)

#dd sorting
charging_sessions = {
    'publicChargers': 1,
    'home': 20,
    'superChargers': 5
}

#sort by location
sort_location = sorted(charging_sessions.items())
print(sort_location)
#sort by type sessions
sort_charging = sorted(charging_sessions.items(), key=lambda x: x[1])
print(sort_charging)

#list of dd
charging_session = [{
    'location': 'home',
    'time': 4,
    'cost': 4.50
}, {
    'location': 'superCharger',
    'time': .3,
    'cost': 8
}, {
    'location': 'home',
    'time': 3,
    'cost': 3.50
}, {
    'location': 'public',
    'time': 4,
    'cost': 0
}, {
    'location': 'home',
    'time': 2,
    'cost': 2.50
}, {
    'location': 'superCharger',
    'time': .2,
    'cost': 8.50
}]

#iterate over the list of dd and output summary data
filter_by_location = [location for location in charging_session if location['location'] == 'home']

print('number of charging at home ' + str(len(filter_by_location)))

#iterate over list of dd and add up all cost of charging
total = 0
for session in charging_session:
    if session['location'] == 'superCharger':
        total = total  + session['cost']

print('cost of supercharging ' + str(total))        
