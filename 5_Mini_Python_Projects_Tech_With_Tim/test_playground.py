import random

thislist = ["apple", "banana", "cherry", "tk"]
count = 0
while count != 120:
    count += 1
    computer_pick = thislist[random.randint(0, 2)]
    print(computer_pick)
