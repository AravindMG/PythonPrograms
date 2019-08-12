# For Loop

# for i in range(1,4):
#     for j in range(1,4):
#         print("Value of i is {}".format(i*j))

# for i in range(1,6):
#     print("value of i is {}".format(i / i))

# numbers = "9, 233, 422, 522, 822"
# for i in range(0, len(numbers)):
#     if numbers[i] in '012345679':
#         print(numbers[i],end='\t')

# numbers = "9, 233, 422, 522, 822"
# cleanedNumber = ''
#
# for char in numbers:
#     if char in '239458':
#         print(numbers)
#        cleanedNumber = cleanedNumber + char

#newNumber = int(cleanedNumber)

# countryList = ['America','India','New Zealand','Australia']
# for countries in countryList:
#     print("This is " + countries)

# multiplication tables

# for i in range(1,9):
#     for j in range(1,11):
#         print("{0} * {1} = {2}".format(i,j,i*j))
#     print("**************")

meal = ["briyani", "chicken65", "Mutton", "eggs"]
no_vegan_option = ''
for item in meal:
    if item == "vegetableBriyani":
        no_vegan_option = item
        break

if no_vegan_option:
    print("I don't like vegan option in my meal")
else:
    print("I like the meal plan")
