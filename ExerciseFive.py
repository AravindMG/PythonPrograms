# printing only the capital letters
#
# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """
#
# upper_chars = ""
#
# for char in quote:
#     if char.isupper() == True:
#         upper_chars += char
# print(upper_chars)

# dvisibleBy7 = []
# for i in range(0,100):
#     print("The numbers that are divisible by 7 is {0} {1}".format(i, i % 7 == 0))

# correct way

for i in range(0, 101, 7):
    print(i)
