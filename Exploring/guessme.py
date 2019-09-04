import random


def main():
    user_input = input("Please enter an alphabet: ")
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    y = random.choice(x)
    print(y)
    if user_input == y:
        print("you guessed it correctly!")
    else:
        print("try again later")


if __name__ == "__main__":
    main()

