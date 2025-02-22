# What are methods?

# dict, str, these are objects in python
# inside the objects, there are methods for recurring situations
# functions linked to the objects

products = {
    'Banana' : 3.60,
    'Milk' : 4.90,
    'Meat' : 15.50,
    'Bread' : 9.00,
}

products.clear()
print(products) # empty dictionary

dir(products) # will show a list of methods of the object

help(products.clear) # to show a description
