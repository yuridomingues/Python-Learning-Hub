# a key and its corresponding value
capitals = {'Brazil': 'Brasília',
            'France': 'Paris', 
            'Japan': 'Tokyo'
}

print(capitals['Brazil'])
<<<<<<< HEAD
# Will show "Brasília"

# Dictionaries are mutable

capitals['England'] = 'London'

print(capitals['England'])
# Will show 'London'

del capitals['England']
# Will delete

for country in capitals:
    capital = capitals[country]
    print(f'The capital of {country} is: {capital}')


d = dict()
d[10] = 'abc'
d['KEY'] = 5
d[3.15] = True

# print(d)

# for k in d:
#    v = d[k]
#    print(f'Key: {k}, Value: {v}')

print(d.items())
=======
>>>>>>> 170fc90 (feat: add in operator)
