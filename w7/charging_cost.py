#Week 7 Learn Together Code
#My code is modeling the concept of charging my electric car

#DD for data related to home charging
homeCharging = {
    'kwhUsed': 20,
    'startTime': '1am',
    'endTime': '5am',
    'cost': 6
}

#add a key to a dd
print(homeCharging.setdefault('peak', False))
#output - False

#check whether a given key already exists in a dd
print(homeCharging.get('kwhUsed', 0))
#output - 20

print(homeCharging.get('totalKWH',0))
#output - 0

print(homeCharging)
#output - {'kwhUsed': 20, 'startTime': '1am', 'endTime': '5am', 'cost': 6, 'peak': False}

#iterate over dd using for loops
for session, values in homeCharging.items():
    print(session, values)
#output - 
# kwhUsed 20
# startTime 1am
# endTime 5am
# cost 6
# peak False

#dd sorting
charging_sessions = {
    'publicChargers': 1,
    'home': 20,
    'superChargers': 5
}

#sort by location
sort_location = sorted(charging_sessions.items())
print(sort_location)
#output - [('home', 20), ('publicChargers', 1), ('superChargers', 5)]

#sort by type sessions
sort_charging = sorted(charging_sessions.items(), key=lambda x: x[1])
print(sort_charging)
#output - [('publicChargers', 1), ('superChargers', 5), ('home', 20)]

sort_charging_reverse = sorted(charging_sessions.items(), key=lambda x: x[1],reverse=True)
#[('home', 20), ('superChargers', 5), ('publicChargers', 1)]
print(sort_charging_reverse)

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
#https://blog.finxter.com/how-to-filter-a-list-of-dictionaries-in-python/

filter_by_location = [session for session in charging_session if session['location'] == 'home']
print(filter_by_location)

#output - [{'location': 'home', 'time': 4, 'cost': 4.5}, {'location': 'home', 'time': 3, 'cost': 3.5}, {'location': 'home', 'time': 2, 'cost': 2.5}]

print('number of charging at home sessions is ' + str(len(filter_by_location)))
#output - number of charging at home sessions is 3

#iterate over list of dd and add up all cost of charging
total = 0
for session in charging_session:
    if session['location'] == 'superCharger':
        total = total  + session['cost']

print('cost of supercharging ' + str(total))        
#output - cost of supercharging 16.5

