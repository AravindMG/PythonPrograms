age = 24
# print("my age is" + str(age) + "years")

print("my age is {0} years".format(age)) # replacement field

print("there are {0} days in {1}".format(31, "January"))

print("my age is %d years" %age)

print("my age is %d %s, %d %s" % (age, "years", 6, "months"))

# for i in range(1, 12):
#     print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

# left aligned if less than symbol is given
for i in range(1, 12):
    print("No. {0} squared is {1:<4} and cubed is {2:<4}" .format(i, i ** 2, i ** 3))