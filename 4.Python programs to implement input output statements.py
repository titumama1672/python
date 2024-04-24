#Write a python program to calculate the area of triangle, circle and rectangle input as run time and display output.

import math as m
a=int (input("enter radius of circle :"))
b=int (input("enter breadth of triangle :"))
c=int (input("(enter height of triangle :"))
d=int (input("enter length of rectangle :"))
e=int (input("enter breadth of rectangle :"))
circle=m.pi*a*a
triangle=0.5*b*c
rectangle=d*e
print(circle)
print(triangle)
print(rectangle)


#Write a python program to take input as a list and tuple and display it.

a=list(input("enter the values"))
b=tuple(input("enter the values"))
print(a)
print(b)



#Write a python program to take a complete sentence as a command line input and display it. also display its length.

name=input("Enter your name :")
print(name)
print(len(name))


#Write a python program to add, subtract, multiply and divide two nos. take input as a command line.

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2) 






