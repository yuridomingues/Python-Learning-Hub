print("Python")
print(type('My name is Yuri!')) # what is the var type of this data?
# <class 'str'>

# str is a sequence of chars

print(type('500')) # <class 'str'>

# if you start with "'" you need to use "'" in the end, the same for the """

print(type(int('5'))) # <class 'int'>

# print(5 + '5') will be a error

print(5 + int('5')) # will be 10

# int values need to be base 10
# so if you try to show a int str, will get a error, like this:
# print(int('Yuri'))

# but you can use str to base 10 numbers
print(type(str(10))) # will show str, and will get none error

print("50" + "10") # will concat the text, isn't a math operation

print("Hello" + " Yuri") # space is a char too
print("30" + "___" + "????") # will concat everything same

print("Python" * 3) # you can multiply a string and concat everything
# but you can't subtract a char in a string with math operation
# print("abc" - "c") will get a error

print(len("Yuri")) # len will show the number of chars between the parenthesis
print(len("              ")) # even if is only spaces

# but len is only for string, if you try to get in something like int numbers, you will get an error
# like this: print(len(5))

# you have the help function too, that will help you to explain functions
# like this: help(print)
