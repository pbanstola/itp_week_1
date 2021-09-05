# ITP Week 1 Day 2 (In-Class) Practice #2

# This is a number magic trick
# Pick a number from 1 - 9
first_num = int(input("Pick a number from 1 - 9 "))
# Multiple by 2
second_num = int(first_num) * 2
# Add 10 to the total
third_num = second_num + 10
# Divide by 2
four_num = int(third_num/2)
# Subtract by the original number
final_num = four_num - first_num
# Final number is 5
print(final_num)
# Take an user's input
# Assign a new variable for each step
# at the end, use an if statement to see if the final is always 5!
if(final_num == 5):
    print("THe final number is always " + str(final_num))
else:
    print('You did calculation process wrong')
