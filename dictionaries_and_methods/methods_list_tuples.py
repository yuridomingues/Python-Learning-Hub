tup = (0, 0, 0, 1, 0, 1, 0)

# Find the index of the first occurrence of 1 in the tuple
print(tup.index(1))

# Count the number of occurrences of 0 in the tuple
print(tup.count(0))

l1 = [0, 0, 1, 0, 1, 0]
l2 = l1.copy()

# Print the original list l1
print(l1)

# Clear the list l1
l1.clear()

# Append numbers from 0 to 8 (exclusive) multiplied by 2 to the list l1
for n in range(5):
    l1.append(n * 2)

# Print the updated list l1
print(l1)

# Append the string 'hello' to the list l1
l1.append('hello')
print(l1)

values = [10, 30, -90, -1, 0, 1]
positive_values = []

# Iterate over the values list and append positive values to the positive_values list
for value in values:
    if value > 0:
        positive_values.append(value)

# Print the positive_values list
print(positive_values)

numbers = [1, 2, 3]

# Append the list [4, 5, 6] as a single element to the numbers list
numbers.append([4, 5, 6])
print(numbers)

numbers = [1, 2, 3]

# Extend the numbers list with the elements [4, 5, 6]
numbers.extend([4, 5, 6])
print(numbers)

numbers = [1, 2, 3]

# Create a new list new_numbers by concatenating numbers and [4, 5, 6]
new_numbers = numbers + [4, 5, 6]
print(new_numbers)

vowels = ['a', 'i', 'o', 'u']

# Insert the letter 'e' at index 1 in the vowels list
vowels.insert(1, 'e')
print(vowels)

values = [150, 20, 30, 40, 50]

# Remove and return the last element from the values list
removed_value = values.pop()
print(removed_value)

# Remove and return the element at index 0 from the values list
removed_value = values.pop(0)
print(removed_value)

customers = ['yuri', 'ana', 'cindy', 'mary jane']

# Process each customer in the customers list by popping them one by one
while customers:
    customer = customers.pop()
    print(f'Processing customer {customer}')

values = [150, 20, 30, 40, 50]

# Reverse the order of elements in the values list
values.reverse()
print(values)

# Sort the values list in ascending order
values.sort()
print(values)