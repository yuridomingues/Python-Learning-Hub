values = [10, 20, 30, 3, -2, 17]

for value in values:
    print(f'The value is: {value}')

print('End of the loop')

name = 'Yuri'

for char in name:
    print(f'The character is: {char}')

print('End of the loop')

clients = [
    ('Ana', 'xxx', 'xxx@email.com'), 
    ('Yuri', 'yyy', 'yyy@email.com')
    ]

#for client in clients:
    #name = client[0]
    #cpf = client[1]
    #email = client[2]
    #name, cpf, email = client
    #print(f'Client: {name}\nCPF: {cpf}\nEmail: {email}\n')

# z = (10, 20)
# x, y = z
# x = 10
# y = 20

# letter1, letter2, letter3 = 'abc'
# letter1 = 'a'
# letter2 = 'b'
# letter3 = 'c'

for name, cpf, email in clients:
    print(f'Client: {name}\nCPF: {cpf}\nEmail: {email}\n')
