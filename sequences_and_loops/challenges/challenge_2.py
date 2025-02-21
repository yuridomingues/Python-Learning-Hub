# Given two lists, print all values that appear
# duplicated in both lists

# Given two lists, print a message indicating whether
# there is any common element between them or not.

first_number_list = [0, 1, 2, 3, 4, 5, 6, 7]
second_number_list = [5, 6, 7, 8, 9, 10, 11]

NUMBER_COMPARATOR = 0
for number in first_number_list:
    NUMBER_COMPARATOR = number
    for number in second_number_list:
        if NUMBER_COMPARATOR == number:
            print(f'This number is duplicated: {number}')


first_list = [10.0, 'xx', True]
second_list = [0, False, 'xx']

COMMON_ELEMENT = False

for element in first_list:
    if COMMON_ELEMENT:
        break
    for comparator in second_list:
        if element == comparator:
            COMMON_ELEMENT = True
            break

if COMMON_ELEMENT:
    print('The first list and the second list have common elements')
else:
    print('There is no common element between the lists')
