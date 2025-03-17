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
# a key and its corresponding value
capitals = {'Brazil': 'Brasília',
            'France': 'Paris', 
            'Japan': 'Tokyo'
}

if 'Brazil' in capitals:
    print('True') # will show true

if 'England' in capitals:
    print('False') # will show false

country = 'Brazil'

if country in capitals:
    country = capitals[country]
    print(f'The capital of {country} is {country}')
else:
    print(f'There is no registered capital for {country}') # The capital of Brazil is Brasília


values = [1, 2, 3]

4 in values
# will show false

text = 'im studying python'

'python' in text 
# will show True

if text not in ('1,', '2'):
    print('Invalid option, write 1 or 2')
