# LIST
###########################################
# ipAddress = input("please enter any ip: ")
# print(ipAddress.count("8"))

# even = [2, 4, 6, 8]
# odd = [1, 3, 7, 9]
#
# numbers = even[0] + odd[1]
# print(numbers)

# list_1 = []
# list_2 = [1, 2, 3, 4]
# list_1.append(list_2)
# print(list_1)


# even = [2, 4, 6, 8]
# odd = [1, 3, 7, 9]
#
# numbers = [even, odd]
#
# for number_set in numbers:
#     print(number_set)
#
#     for value in number_set:
#         print(value)

# menu = []
# menu.append(['egg', 'spam', 'sausage'])
# menu.append(['egg', 'sausage', 'bacon'])
# menu.append(['egg', 'spam'])
# menu.append(['egg', 'bacon', 'spam'])
# menu.append(['egg', 'bacon', 'sausage', 'spam'])
# menu.append(['spam', 'bacon', 'sausage', 'spam'])
# menu.append(['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'])
# menu.append(['spam', 'egg', 'sausage', 'spam'])
#
# for meal_list in menu:
#     print(meal_list)
#
#     for meal in meal_list:
#         if not 'spam' in meal_list:
#             print(meal)
################################################
# ITERATORS
################################################

# string = "1234567890"
# my_iterator = iter(string)
# print(next(my_iterator))
#
# for char in iter(string):
#     print(char)

# my_list = [1, 2, 3, 4, 5, 6, 7]
# my_iterator = iter(my_list)
#
# for i in range(0, len(my_list)):
#     next_item = next(my_iterator)
#     print(next_item)
################################################
# Range
################################################

# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd[2])

# print(range(0, 5, 2) == range(0, 6, 2))
# print(list(range(0, 5, 2)))
# print(list(range(0, 6, 2)))

# r = range(0, 100)
#
# for i in r[::-2]:
#     print(i)

################################################
# Challenge
################################################

# o = range(0, 100, 4)
# print(o)
# p = o[::5]
# print(p)
# for i in p:
#     print(i)

################################################
# Tuples
################################################

# unpacking the tuple
# values = ("1", "2", "3")
# a, b, c = values
# print(a)
# print(b)
# print(c)

# imelda = "More Mayhem", "Imelda May", 2011, (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# print(imelda)
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# for songs in tracks:
#     track_number, title = songs
#     print("\tTrack Number: {}, Title: {}".format(track_number, title))
