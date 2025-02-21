# Given a sequence of numbers, calculate the sum and average of the numbers.
# Note: You cannot use the sum() function!

# Given a sequence of numbers, calculate the largest value in the sequence.
# Note: You cannot use the max() function!

# Given a list of words, print all the words with at least 5 characters.

number_sequence = [10, 30, -8, 0, -2, 4]

SEQUENCE_SUM = 0

for n in number_sequence:
    SEQUENCE_SUM += n
print(f'The sum of the {number_sequence} is: {SEQUENCE_SUM}')
# print(sum(number_sequence))

SEQUENCE_AVERAGE = SEQUENCE_SUM / len(number_sequence)
print(f'The average of this sequence is: {SEQUENCE_AVERAGE}')

SEQUENCE_LARGEST = number_sequence[0]

for number in number_sequence:
    if number > SEQUENCE_LARGEST:
        SEQUENCE_LARGEST = number
print(f'The largest number in {number_sequence} is {SEQUENCE_LARGEST}')
# print(max(number_sequence))

words_list = ['yuri', 'ana', 'mary jane', 'cindy']

for word in words_list:
    if len(word) <= 5:
        print(word)
