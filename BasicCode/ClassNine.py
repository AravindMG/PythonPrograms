# While Loop

# for i in range(10):
#     print("i is now {}".format(i))
# i = 0
# while i <= 10:
#     print("i is now {}".format(i))
#     i += 1

# exiting a place, using a while loop

# available_exits = ["east", "west", "north", "south"]
# print(available_exits)
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("please choose a direction: ")
#
# print("You are moving on to another area")

# Guessing game

import random

max_number = 10
answer = random.randint(2, max_number)

# print(answer)

print("please guess a number between 2 and {}: ".format(max_number))

guess = int(input())

if guess != answer:
    if guess > answer:
        print("please guess a lower number")
    else:
        print("please guess a higher number")
    guess = int(input())
    if guess == answer:
        print("Congratulations")
    else:
        print("Try again later")
else:
    print("Hooray! got it in first try")


