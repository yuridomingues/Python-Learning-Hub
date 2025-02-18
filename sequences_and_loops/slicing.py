people = ['João', 'Paulo', 'Clara', 'Maria']

"""
This script demonstrates the usage of slicing in Python.

Slicing is a technique in Python that allows you to extract a portion of a sequence, such as a list or a string, by specifying a starting point and an ending point. The slice includes all elements from the starting point up to, but not including, the ending point.

In this script, we have a list called 'people' containing the names of individuals. We demonstrate slicing by printing out specific elements and a range of elements from the list.

Example usage:
    - Printing a specific element:
        print(people[1])  # Output: Paulo

    - Slicing a range of elements:
        print(people[1:3])  # Output: ['Paulo', 'Clara']
"""

print(people[1])

# Slicing

# It sets a starting point and an ending point and iterates through it
print(people[1:3])

# If you want to know how much strings will return in the slicing, just make a subtraction like 3 - 1 = 2

print(len(people)) # will return 4

list_people = people[0:len(people)]
print(list_people) # will show everyone in the list, but can be this way too in python

print(people[0:]) # python know the last one is the end 
print(people[:4]) # python know the first one is the first

name = 'yuri'

print(name[0:]) # will show yuri

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[0:len(numbers):2]) # will return in two by two element, the third item in the slice is know by jump
print(numbers[::2]) # will show the same

print(numbers[::-1])