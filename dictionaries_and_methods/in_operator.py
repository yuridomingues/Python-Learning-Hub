capitals = {
    'Brasil' : 'Brasilia',
    'France' : 'Paris',
    'Japão' : 'Tóquio'
}

print('Brasil' in capitals) # will show True
print('Brasília' in capitals) # will show False, only key

country = 'England'

if country in capitals:
    capital = capitals[country]
    print(f'The capital of {country} is {capital}')
else:
    print(f'There is no capital registered to {country}')

values = [1, 2, 3]

print(3 in values) # True
print(4 in values) # False

text = 'i am studying python'
print('python' in text) # True