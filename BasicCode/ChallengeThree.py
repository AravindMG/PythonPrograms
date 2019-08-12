# Guessing game with while loop

import random

max_number = 10
answer = random.randint(2, max_number)
print(answer)
print("please guess a number between 2 and {}: ".format(max_number))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("Guess a higher number")
    elif guess > answer:
        print("guess a lower number")
    else:
        print("Congrats! you guessed it")


