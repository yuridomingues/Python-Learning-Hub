# Dictionary of products and prices
products = {
    "Rice": 20.50,
    "Beans": 7.30,
    "Pasta": 4.20,
    "Olive Oil": 15.00,
    "Coffee": 8.50,
    "Sugar": 3.80,
    "Milk": 4.50,
    "Bread": 5.00,
    "Butter": 6.70,
    "Cheese": 12.00
}

# products.clear() will clear the dict

products.get('Rice') # will show the value

# if you want to get but don't know if exists
print(products.get('Strawberry', "Not found"))

products.setdefault('Strawberry', 100) # will insert the key and value

for product in products.keys(): # sequence of keys
    print(product)

for value in products.values():
    print(value) # will show the values

for pair in products.items():
    print(pair) # will show the key and value

for k, v in products.items():
    print(f'{k} -> {v}') # will show the key and value

# if doesn't exist, will add and if exists, will update the value

new_products = {
    'kiwi' : 5.70,
    'Strawberry' : 4.40,
}

products.update(new_products)
print(products)

products_copy = products.copy() # will copy the dict and not change the original
products_copy['orange'] = 3.30

print(products_copy)