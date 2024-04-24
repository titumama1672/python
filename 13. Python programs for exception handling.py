#13. Python programs for exception handling.

try:
    age = int(input("Please Enter your Age:"))
except ValueError:
    age= -1
if age >=0 and age <= 100:
    print("This is a valid age")
else:
    print("That is Invalid age")
