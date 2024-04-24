#ii. Write a python program for (a) add two integers (b) add two floats (c) add two complex

a = 5
b = 10
sum_integers = a + b
print("Sum of integers : ", sum_integers)
x = 3.14
y = 1.618
sum_floats = x + y
print("Sum of floats : ", sum_floats)
z = 2 + 3j
w = 1 - 4j
sum_complex = z + w
print("Sum of complex numbers : ", sum_complex)


#Write a python program to convert numbers from octal, binary and hexadecimal system to decimal no. system.

octal_num = '13'
decimal_num = int(octal_num, 8)
print("Decimal equivalent of", octal_num, "is ", decimal_num)
binary_num = '10101'
decimal_num = int(binary_num, 2)
print("Decimal equivalent of", binary_num, "is ", decimal_num)
hex_num = '1a'
decimal_num = int(hex_num, 16)
print("Decimal equivalent of", hex_num, "is ", decimal_num)


#Write a python program to implement identity and membership operators.


x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)
print(x is z)
print(x is not y)
print(x is not z)
a = [1, 2, 3, 4, 5]
b = 3
c = 6
print(b in a)
print(c in a)
print(b not in a)
print(c not in a)
