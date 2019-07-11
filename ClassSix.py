# program flow control

# if and elif statements

# name = input("please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
#
# if age >= 18:
#     print("You are legally allowed to vote")
# else:
#     print("Come back in {} years".format(18 - age))
#
# print(age)

# print("Hello {0} ".format("Aravind") + " welcome to Guessing Game: ")
# print("Guess the numbers between 1 to 10")
#
# guess = int(input())
#
# if guess < 5:
#     print("Please guess a higher number")
#     guess = int(input())
#     if guess == 5:
#         print("Well done! You Guessed it")
#     else:
#         print("Sorry try again later")
# elif guess > 5:
#     print("please guess a lower number")
#     guess = int(input())
#     if guess == 5:
#         print("Well done! you guessed it")
#     else:
#         print("Sorry try again later")
# else:
#     print("Hooray!You go it the first time")

# age = int(input("How old are you? "))
#
# if 16 <= age <= 65:
#     print("Have a good day at work!")
# else:
#     print("Enjoy your free time")
#
# x = "true"
# if x:
#     print("x is true")

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("Give me an {}, bob".format(letter))
else:
    print("Letter not found in parrot")