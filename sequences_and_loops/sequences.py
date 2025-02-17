# Strings are sequences too

name = "yuri"

print(name[0])  # This will print the first character of the string 'name', which is 'y'

list_numbers = [1, 2, 3]  # This creates a list with the elements 1, 2, and 3
tuple_list_numbers = tuple(list_numbers)  # This converts the list into a tuple

list_from_tuple = list(tuple_list_numbers)  # This converts the tuple back into a list

str_list_numbers = str(list_numbers)  # This converts the list into a string
print(list_numbers)  # This prints the original list

list_from_name = list(name)  # This converts the string 'name' into a list of characters
print(name)  # This prints the original string

s = ""  # This creates an empty string
print(len(s))  # This prints the length of the empty string, which is 0

li = []  # This creates an empty list
print(len(li))  # This prints the length of the empty list, which is 0

tup = ()  # This creates an empty tuple
print(len(tup))  # This prints the length of the empty tuple, which is 0

print(str())  # This prints an empty string
print(list())  # This prints an empty list
print(tuple())  # This prints an empty tuple

print(bool(10))  # This prints True because 10 is a non-zero number
print(bool(''))  # This prints False because the string is empty
print(bool('asldkasldkas'))  # This prints True because the string is non-empty

# bool will return true if there is something
# bool will return false if there is nothing

seq = [1, 2, 3]

# In Python, an empty list evaluates to False, and a non-empty list evaluates to True
if seq:
    # This block will execute if 'seq' is not empty
    print("Sequence is not empty")
else:
    # This block will execute if 'seq' is empty
    print("Sequence is empty")
