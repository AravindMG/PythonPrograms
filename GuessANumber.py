import random

numberRandom = random.randint(1, 21)*5
print(numberRandom)
name = input("Please enter your name: ")
number = int(input("Hello " + name + " Please Guess a number: "))

if number == numberRandom:
    print("Hooray! You Guessed it " + name)
elif number <= numberRandom:
    print("Please guess a higher number next time")
elif number >= numberRandom:
    print("Please guess a lower number next time")

number = int(input(name + " You Have one more guess: "))

if number == numberRandom:
    print("Hooray! You Guessed it " + name)
else:
    print("Sorry " + name + " please try again later")
