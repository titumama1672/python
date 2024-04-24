"""Write a python program to create string and display 0 th character, display 3 rd to
6 th character, display 6 th character onwards, display last character, print the
string twice and concatenate two strings."""


str1 = "Hello, World!"

print("0th character:", str1[0])

print("3rd to 6th character:", str1[2:6])

print("6th character onwards:", str1[5:])

print("Last character:", str1[-1])

print("String printed twice:", str1 * 2)

str2 = " Have a nice day!"
concatenated_string = str1 + str2
print("Concatenated string:", concatenated_string)


#Write a python program to implement list tuple and set,

my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

my_list.append(6)
print("List after adding an element:", my_list)

my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

print("First element of tuple:", my_tuple[0])

my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

my_set.add(6)
print("Set after adding an element:", my_set)


#Write a python program to implement a dictionary, print its keys and values.

# Create a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

print("Dictionary:", my_dict)

print("Keys:", my_dict.keys())

print("Values:", my_dict.values())




#Write a python program to implement range ().

print("Using range() in a for loop:")
for i in range(5):
    print(i)

print("\nUsing range() with start and end parameters:")
for i in range(5, 10):
    print(i)

print("\nUsing range() with start, end, and step parameters:")
for i in range(0, 10, 2):
    print(i)
