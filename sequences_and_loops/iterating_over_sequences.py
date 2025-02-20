values = [10, 20, 30, 3, -2, 17]

for value in values:
    print(f'The value is: {value}')

print('End of the loop')

name = 'Yuri'

for char in name:
    print(f'The char is: {char}')

print('End of the loop')

clientes = [
    ('Ana', 'xxx', 'xxx@email.com'), 
    ('Yuri', 'yyy', 'yyy@email.com')
    ]

#for cliente in clientes:
    #nome = cliente[0]
    #cpf = cliente[1]
    #email = cliente[2]
    #nome, cpf, email = cliente
    #print(f'Cliente: {nome}\nCPF: {cpf}\nEmail: {email}\n')

# z = (10, 20)
# x, y = z
# x = 10
# y = 20

# letra1, letra2, letra3 = 'abc'
# letra1 = 'a'
# letra2 = 'b'
# letra3 = 'c'

for nome, cpf, email in clientes:
    print(f'Cliente: {nome}\nCPF: {cpf}\nEmail: {email}\n')
