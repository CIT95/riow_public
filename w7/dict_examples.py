data = {
    'color': 'red',
    'fruit': 'apple',
    'species': 'dog'
}

for thing in data:
    print(thing)

for key in data: 
    print(key, data[key])

for value in data.values():
    print(value)

for key, value in data.items():
    print(key, value)    

for item in data.items():
    print(item)

data.setdefault('task', 'new')    
print(data)



