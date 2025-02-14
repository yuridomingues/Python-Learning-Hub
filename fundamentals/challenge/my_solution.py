# Challenge - create a program that:
# - Asks for your name and age
# - Greets you
# - Counts how many letters your name has
# - Tells you how old you will be in 5 years

name = input("Please write your name: ")
age = input("Please write your age: ")

print("Hello " + name + " with the " + age + " age")

name_letters = len(name)
five_years_age = int(age) + 5

print("You will be " + str(five_years_age) + " age in 5 years")