# Task 1. Create a variable called `fruits` and one after another add the elements `Apples`, `Cherries` and `Strawberries`. 
# Loop over the list `fruits` and print every element to the screen.

print('Task 1')
fruits = ['Apples', 'Cherries', 'Strawberries']
for fruit in fruits: # for every fruit in the list fruits (3 times) print a fruit
  print(fruit)



# Task 2. Create a variable `cities` which holds a list with the cities `London`, `Paris`, `Berlin` and `Amsterdam`.
# Print the sentence `The capital city of Germany is: Berlin` to the screen, using the string `Berlin` from the cities array.

print('\nTask 2')
cities = ['London', 'Paris', 'Berlin', 'Amsterdam']
print(f'The capital city of Germany is: {cities[2]}')



# Task 3 Store the colors `cyan`, `magenta`, `green`, `yellow`, `black` and `white` in a list called `colors`.
# Remove the colors `green` and `white`. Print the remaining colors to the screen.

print('\nTask 3')
colors = ['cyan', 'magenta', 'green', 'yellow', 'black', 'white']
colors.remove('green')
colors.remove('white')
colors = ', '.join(colors) # this removes the brackets and commas from the list and add whatever we want in between the elements
print(colors)



# Task 4 Store the letters `p`, `e`, `n`, `g`, `u`, `i`, `n` in a list.
# Combine those letters into a single string `penguin`. Capitalize that string and print it to the screen.

print('\nTask 4')
penguin = ['p', 'e', 'n', 'g', 'u', 'i', 'n']
penguin = ''.join(penguin) # this removes the brackets and commas from the list and add whatever we want in between the elements
penguin = penguin.capitalize()
print(penguin)


