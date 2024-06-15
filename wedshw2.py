# The Range Riddle

# Every other day

days_of_the_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
days_of_the_week[0] = "sunday"
for i in range(len(days_of_the_week)):
    if i % 2 == 0:
        print(days_of_the_week[i])
# Loop Condition Logic

# Conditional Exit
item = []

while True:
    user_input = input("what is your desired item?: or type done when finished:")
    if user_input == "done":
        print(item)
        break
    else:
        item.append(user_input)

# Pythons's Random Game Night
import random
items = ["cross, holy water, stake, sword,broom"]
computer_choice = random.choice(items)
while True:
    user_choice = input("Please select item, cross, holy water, stake, sword, broom:")
    computer_choice = random.choice(items)
    if user_choice == computer_choice:
        print("We have a Winner!!!")
    elif user_choice != computer_choice:
        print("Better Luck Next Time!!!")
    else:
        print(input("Try Again:"))

