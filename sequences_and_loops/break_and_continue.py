n = 0

while n < 10:
    print(f'The value of n is: {n}')
    n += 1
    if n == 5:
        break  # Exit the loop when n equals 5

print('The loop is over')

for n in range(-5, 6):
    if n == 0:
        continue  # Skip the rest of the loop body when n equals 0
    result = 1 / n
    print(f'The result is: {result}')

print('The loop is over')

while True:
    opt = input('Choose an option (1, 2) | "q" to quit: ')
    print(f'The entered option was: {opt}')
    if opt == 'q':
        break
    elif opt != '1' and opt != '2':
        print("Invalid option")
        continue
    print(f'Option selected: {opt}')

print('Program finished')
