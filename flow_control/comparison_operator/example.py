hungry = input("Are you hungry? (write yes for yes): ")

if hungry.lower() == "no":
    exit()

elif hungry.lower() == "yes":
    has_food = input("Do you have food in your house? (write yes for yes): ")
    if has_food.lower() == "yes":
        print("Preparing a meal\nEating the food..")
        exit()
    if has_food.lower() == "no":
        print("Going to the market\nReturning home\nPreparing a meal\nEating the food..")
        exit()

# lower will make the str will be write in lowercase