# You can modify a list

students = ['Ana', 'Yuri', 'MJ', 'Cindy']

# Replace 'Yuri' with '4'
students[1] = '4'
print(students)  # Output: ['Ana', '4', 'MJ', 'Cindy']

# You can delete an element from the list too

# Delete the element at index 1 ('4')
del students[1]
print(students)  # Output: ['Ana', 'MJ', 'Cindy']

# Tuples

# Define a tuple
tuples = (1, 2, 3)
print(type(tuples))  # Output: <class 'tuple'>

# A tuple is like an immutable list
