input() # this function will wait to the user insert a input

# you can insert the input to a variable

x = input()
print('The input value is : ' + x) # the plus will concat the string to the variable and the variable will show the input value

# you can write something in the console for oriented user experience

y = input("Insert a number: ")
print('The number is: ' + y)

# you can convert the string value to a int and sum the result too

x_num = int(x)
print(x_num + 4)

# you can't write numbers in the input and try to sum, because letters isn't base 10

# you can define the type like this too
z = int(input("Insert a number: "))
print(z + 10)