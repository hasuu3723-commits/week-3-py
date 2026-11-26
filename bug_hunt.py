
# Python Week 3 Assignment - Bug Hunt

count = 1
total = 0

# BUG 1: Added a colon (:) after the while condition.
# BUG 2: Changed count < 5 to count <= 5 so the loop includes 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG 3: Converted total to a string using str()
# because Python cannot directly join a string and an integer.
print("Sum of 1 to 5 is: " + str(total))
