lista = [1, 2, 3]
print(type(lista))  # Output the type of 'lista', which is <class 'list'>

# Lists are sequences and can hold any type within them

mixed_list = [0, 1.1, "Yuri", True, [4, 6]]
print(mixed_list)  # Output the mixed_list containing different data types

students = ['Yuri', 'Ana', 'MJ', 'Cindy']
sales = [50, 40, 45, 30]

# Indexing: you can get elements from the list, the first element is always at index 0

print(mixed_list[0])  # Output the first element of mixed_list, which is 0

# Getting the last element of the 'students' list

print(students[len(students) - 1])  # Output the last element of students using len()

# In Python, it can be easier

print(students[-1])  # Output the last element of students using negative indexing

# If you want to pick the last element of the list inside a list

print(mixed_list[-1][-1])  # Output the last element of the last list inside mixed_list, which is 6