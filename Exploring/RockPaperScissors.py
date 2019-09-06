# rock, paper, scissors game


import random


def game():
    while True:
        user_input = input("Please choose any one, 'rock', 'paper', 'scissors': ")
        choice_for_computer = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choice_for_computer)
        print(computer_choice, "\n")
        if user_input == 'rock' and computer_choice == 'scissors':
            print("Rock beats scissors! You win")
        elif user_input == 'rock' and computer_choice == 'paper':
            print("Paper crushes rock! Computer wins")
        elif user_input == 'paper' and computer_choice == 'rock':
            print("Paper crushes rock! You win")
        elif user_input == 'paper' and computer_choice == 'scissors':
            print("scissors cuts paper! computer wins")
        elif user_input == 'scissors' and computer_choice == 'rock':
            print("Rock beats scissors! computer wins")
        elif user_input == 'scissors' and computer_choice == 'paper':
            print("scissors cuts paper! you win")
        user_input2 = input("Do you want to continue playing(y/n): ")
        if user_input2 == 'y':
            continue
        elif user_input2 == 'n':
            print("Thanks for Playing, come back soon!")
            break


if __name__ == "__main__":
    game()
