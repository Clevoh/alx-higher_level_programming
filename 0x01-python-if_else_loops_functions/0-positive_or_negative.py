#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# Check whether the number is positive, zero, or negative
if number > 0:
    result = "is positive"
elif number == 0:
    result = "is zero"
else:
    result = "is negative"

# Print the number and its status
print(f"The number {number} {result}\n")

