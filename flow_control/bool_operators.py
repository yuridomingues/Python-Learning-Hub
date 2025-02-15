# Ask the user if they are hungry
im_hungry = input('I am hungry? ')

# Ask the user if they have food
have_food = input('I have food? ')

# Check if the user is hungry and does not have food
if im_hungry and not have_food:
    # If true, print the steps to get food and eat
    print('Going to the market\nGoing home\nMaking a melt\nEat the food')

# Check if the user is hungry and has food
if im_hungry and have_food:
    # If true, print the steps to make and eat the food
    print('Making a melt\nEat the food')