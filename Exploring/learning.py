def add_numbers(x, y):
    sum = x + y
    return sum


def subract_numbers(x, y):
    subract = x - y
    return subract


def ask_input():
    x = int(input("enter the first number \n"))
    y = int(input("enter the second number \n"))
    print("The sum of two numbers is", add_numbers(x, y))
    print("The subtraction of two numbers is", subract_numbers(x, y))


if __name__ == "__main__":
    ask_input()
