"""8. Python programs to implement functions.

i. Write a python program to create a function to check whether given no. is
prime or not.
ii. Write a python program to create a function that returns multiple results as
addition, subtraction, multiplication and division.
iii. Write a python program to create a recursive function for the factorial of a
given number using recursion.
iv. Write a python program to create a recursive function to generate Fibonacci
series."""

#1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(12))


#2
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
def Arithmetic(a,b):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add,sub,mul,div
c= Arithmetic(a,b)
print(c)



#3
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(2))
print(factorial(8))


#4
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(9))
