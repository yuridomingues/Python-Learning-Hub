# """Range Function"""

# The range function generates a sequence of numbers.

# This line prints a list of numbers from 0 to 9.
print(list(range(10)))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# This line creates a list of numbers from 0 to 10.
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# This line prints a sublist of numbers from index 1 to 4 (excluding 5).
print(numbers[1:5])  # Output: [1, 2, 3, 4]

# This line prints a list of numbers from 1 to 4.
print(list(range(1, 5)))  # Output: [1, 2, 3, 4]

# This line prints a sublist of numbers from index 0 to 9 (excluding 10) with a step of 2.
print(numbers[0:10:2])  # Output: [0, 2, 4, 6, 8]

# This line prints a list of numbers from 0 to 10 with a step of 2.
print(list(range(0, 10, 2)))  # Output: [0, 2, 4, 6, 8]

# The % operator returns the remainder of a division.
# The // operator performs integer division (returns the quotient without the remainder).
