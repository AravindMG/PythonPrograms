# def name():
#     user_input = input("Please enter your name: ")
#     return user_input
#
#
# def greet():
#     print("Hello " + name() + ". Good Noon!")
#
#
# if __name__ == "__main__":
#     greet()

def main():
    # Program to filter out only the even items from a list

    my_list = [1, 5, 4, 6, 8, 11, 3, 12]

    new_list = list(map(lambda x: (x * 2), my_list))

    # Output: [4, 6, 8, 12]
    print(new_list)


if __name__ == "__main__":
    main()
