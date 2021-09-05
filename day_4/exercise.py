# ITP Week 1 Day 4 Exercise


# Dictionary Loop

from typing import ValuesView


inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 1
}

# SCENARIO: A person came in and bought one of everything!

del inventory["soda_cans"]
print(inventory)

for item in inventory:
    inventory[item]-=1
    
print(inventory)

    # decrement item by using an assignment operator (Day 2 Lecture line #130)

    # NOTE: recall that item represents the key of the key:value pair

# SCENARIO: REMOVE ANY 0 ITEMS

for item in list(inventory):
    if inventory[item] ==0:
        del inventory[item]
print(inventory)

# {'chips': 12, 'sandwiches': 34, 'candy': 1}
# {'chips': 11, 'sandwiches': 33, 'candy': 0}
# {'chips': 11, 'sandwiches': 33}

    # use an if statement to check if the value is 0 and then remove it
