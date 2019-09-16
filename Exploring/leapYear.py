def leapYear():
    user_input = int(input("Please enter a year(YYYY): "))
    if user_input % 4 == 0:
        print("The provided year is a leap year")
    else:
        print("The provided year is not a leap year")


if __name__ == "__main__":
    leapYear()
