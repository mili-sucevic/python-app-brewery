# List states of America
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# String Concatenation
# states_of_america.append("MiliLand")
# states_of_america.extend(["Mililand", "Testland"])

# Printing Strings
# states_of_america[-1] = "TEST"
# print(len(states_of_america))

# num_of_states = len(states_of_america) - 1
# print(states_of_america[num_of_states])

# Nested Lists
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes","Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# Quiz Q2
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)

# Quiz Q3
dirty_dozen = [fruits, vegetables]

## EXAMPLES ##
# Print out both fruits and vegetables lists
print(dirty_dozen)

# Print out just fruits list
print(dirty_dozen[0])

# Print out just vegetables list
print(dirty_dozen[1])

# Print out the 2nd item from the second list (vegetables)
print(dirty_dozen[1][1])

# Print out the 3rd item from the second list (vegetables) 
print(dirty_dozen[1][2])

# Print out the 4th item from the second list (vegetables) 
print(dirty_dozen[1][3])
