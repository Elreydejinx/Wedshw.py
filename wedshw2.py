# The Range Riddle

# Every other day

days_of_the_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
days_of_the_week[0] = "sunday"
for i in range(len(days_of_the_week)):
    if i % 2 == 0:
        print(days_of_the_week[i])
# Loop Condition Logic

# Conditional Exit

Hottiness = 6
while Hottiness > 5:
    print("your to hot I can't afford you")
    break
else:
    print("ok i can work with that")