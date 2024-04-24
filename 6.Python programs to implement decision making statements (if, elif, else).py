#Write a python program to check whether the entered number is even or odd.
a=int(input("Enter a number to check Even or Odd :"))
if(a%2==0):
    print(a, " is Even")
else:
    print(a, "is Odd")


#Write a python program to enter 5 subject marks and display results (first, second,pass,fail).

a=int(input("Marks of AT"))
b=int(input("Marks of CNND"))
c=int(input("Marks of COA"))
d=int(input(" Marks of OS"))
e=int(input("Marks of EM"))
Total=a+b+c+d+e
Avg=Total/5
if(Avg>90):
    print("First Class")
elif(Avg>80 and Avg<=90):
    print("Second Class")
elif(Avg<=80 and Avg>=35):
    print("Pass")
else:
    print("Fail")


