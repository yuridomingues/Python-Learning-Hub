# To have a newline space in the end, you can use \n
print('-' * 30)
name = input("What is your name?\nInsert here: ")
print(f'Hello, {name}!') # in this way, you don't need to use 
# + to concat string

print(f'Your name has {len(name)} letters')
print(f'Your name has {len(name):.2f} letters') # in this way, you
# will get a float with 2 decimal

# :03d will get 3 chars and plus 0 in the start

print(f'Your name has {len(name):03d} letters')

# you can write a brute string too, like this:

age = input(r"What is your name?\nInsert here: \n\n\naqui")
print('-' * 30)
# like this, you can use \n in the string if you want, or other things