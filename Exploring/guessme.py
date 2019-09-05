import random


def main():
    user_input = input("Please enter an alphabet: ")
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    y = random.choice(x)
    # print(y)
    if user_input == y:
        print("you guessed it correctly!")
    elif user_input != y:
        confirmation = input("Do you want to continue playing(yes/no): ")
        if confirmation == 'no':
            print("Please come back soon!")
        elif confirmation == 'yes':
            user_input2 = input("please guess again: ")
            if user_input2 == y:
                print("You guessed it the second time")
            else:
                print("Better luck next time!")


if __name__ == "__main__":
    main()
