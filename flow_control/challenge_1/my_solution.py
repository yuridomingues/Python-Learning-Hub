# Challenge: create a program that:
#
# Asks for a username and a password
# If both are correct, displays a success message
# Otherwise, displays an error message. The message is different 
# when the username is incorrect and when the password is incorrect
# The "correct" username/password can be defined 
# as variables within the code itself

correct_username = "admin"
correct_password = "1234"

username = input("Your username: ")
password = input("Your password: ")

if username == correct_username and password == correct_password:
    print("Success!")
elif username != correct_username:
    print("Error: Incorrect username.")
elif password != correct_password:
    print("Error: Incorrect password.")
