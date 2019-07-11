# x = 5
# y = 7
#
# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# else:
#     print("x is equal to y")

name = input("Please enter your name: ")
age = int(input("What is your age? "))

if (age >= 18) and (age <= 30):
    print("Welcome " + name + " ,to the holiday trip!")
else:
    print(name + " please join the holiday trip relevant to your age")