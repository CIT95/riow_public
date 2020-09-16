homeCharging = {
    'kwhUsed': 20,
    'startTime': '1am',
    'endTime': '5am',
    'cost': 6
}

print(homeCharging.setdefault('peak', False))
print(homeCharging)

for session, values in homeCharging.items():
    print(session, values)

print(homeCharging.get('kwhUsed', 0))

charging_sessions = {
    'home': 20,
    'superChargers': 5,
    'publicChargers': 1
}

sort_charging = sorted(charging_sessions.items(), key=lambda x: x[1])
print(sort_charging)

