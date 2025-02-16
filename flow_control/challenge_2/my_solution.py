# Challenge - create a program that:
# chooses a secret number
# asks for a guess from the user
# indicates if the user guessed correctly or not
# if not, gives a hint, saying if the number is higher or lower
# repeats this up to 3 times!

secret_number = 4
found_secret = False

if not found_secret:
    user_guess = int(input("What is the secret number? "))
    if user_guess > secret_number:
        print("Is a lower number")
    elif user_guess < secret_number:
        print("Is a higher number")
    else:
        print("You guessed correctly!")
        found_secret = True

if not found_secret:
    user_guess = int(input("What is the secret number? "))
    if user_guess > secret_number:
        print("Is a lower number")
    elif user_guess < secret_number:
        print("Is a higher number")
    else:
        print("You guessed correctly!")
        found_secret = True

if not found_secret:
    user_guess = int(input("What is the secret number? "))
    if user_guess > secret_number:
        print("Is a lower number")
    elif user_guess < secret_number:
        print("Is a higher number")
    else:
        print("You guessed correctly!")
        found_secret = True

if found_secret:
    print("Congratulations! You won the game!")
else:
    print(f"Unfortunately, you lose the game, the secret number is {secret_number}")