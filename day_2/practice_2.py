# ITP Week 1 Day 2 (In-Class) Practice #2

# This is a number magic trick
# Pick a number from 1 - 9
# Multiple by 2
# Add 10 to the total
# Divide by 2
# Subtract by the original number
# Final number is 5

# Take an user's input
step_1 = input("Pick a number from 1 - 9: ")
print("The user selected: " + step_1)
# Assign a new variable for each step
int_step_1 = int(step_1)
print("Casting step 1 as an int: ")
print(int_step_1)

# Multiple by 2
step_2 = int_step_1 * 2
print("Step 2 is type: ")
print(type(step_2))
print("THIS IS STEP 2")
print(step_2)

# Add 10 to the total
step_3 = step_2 + 10
print("STEP 3 BELOW")
print(step_3)

# Divide by 2
step_4 = step_3 / 2

# Subtract by the original number

step_5 = step_4 - int_step_1
# Final number is 5
print(step_5)

# at the end, use an if statement to see if the final is always 5!
if step_5 == 5:
    print("I guess this does work")
else:
    print("its a hoax")