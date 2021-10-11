population = {'Dhaka' : 100, 'Rajshahi' : 90, 'Cox\'s Bazar' : 30}

print(population)
print(sorted(population))
print(list(population))

print(population['Dhaka'])
print('Dhaka' in population)

if 'Dhaka' in population:
    print("Dhaka is a city")

dict([('Google', 'Silicon Valley'), ('Apple', 'Palo Alto'), ('Microsoft', 'Seattle')])

# Generate dictionary using compreshension

phone_names = ['iPhone', 'S20', 'OnePlus']
phone_price = [100, 90, 60]

phones = {x : y for x in ('iPhone', 'S20', 'OnePlus') for y in (100, 90, 60)}

phones2 = {x : y for x in phone_names for y in phone_price}

print(phones)
print(phones2)

# Looping a dictionary
print('\nLoopping in python dictionary:')

for key, value in population.items():
    print(key, value)

# retriving the positions & value using enumerates
print('\nEnumerate:')
for index, value in enumerate(phone_names):
    print(index, value)

print('\nEnumerate for map:')
for index, value in enumerate(phones):
    print(index, value)

# Formatting function is mainly use to format strings or outputs

txt1 = 'My name is {fname}, I\'m {age} years old'.format(fname = 'Jubaer', age = 25)
txt2 = 'I live in {0}, in {1}'.format('Dhaka', 'Mirpur')
txt3 = 'I use an {} but I also like {} whose price is {}'.format(phone_names[0], phone_names[1], phones[phone_names[1]])

# Iterate over two lists using zip():
print('\nIterate over two lists using zip():')
for name, price in zip(phone_names, phone_price):
    print("The price of an {} is {}".format(name, price))
    
# Loop over a sequence in sorted order
print("\nLoop over a sequence in sorted order:")
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

# Using set in a sequence eliminates duplicates
print()
for i in sorted(set(basket)):
    print(i) # Only prints unique elements

# Filtering an array and putting the filtered value in a new arry

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print('\n', filtered_data)