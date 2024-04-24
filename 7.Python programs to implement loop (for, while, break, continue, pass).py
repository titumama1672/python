"""7. Python programs to implement loop (for, while, break, continue, pass).
i. Write a python program to display even nos from n to m.
ii. Write a python program to find the sum of integers present in the list.
iii. Write a python program to display pascal triangles.
iv. Write a python program to print prime numbers up to a given number."""

#1
n=int(input("Starting No : "))
m=int(input("Ending No : "))
for i in range(n,m):
    if i % 2 == 0:
        print(i)



#2
def sum_of_list(l):
    total = 0
    for val in l:
        total = total + val
    return total


my_list = [1,3,5,2,4]
print( "The sum of my_list is", sum_of_list(my_list))


#3
def print_pascal_triangle(n):
    # Initialize the 2D list with zeroes
    triangle = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the triangle
    for line in range(n):
        for i in range(line + 1):
            # First and last values in every row are 1
            if(i == 0 or i == line):
                triangle[line][i] = 1
            # Other values are sum of values just above and left of above
            else:
                triangle[line][i] = triangle[line - 1][i - 1] + triangle[line - 1][i]

    # Print the triangle
    for line in range(n):
        print(' '.join(str(triangle[line][i]) for i in range(line + 1)))

# Test the function
print_pascal_triangle(5)

#4

def print_primes(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
            break
        if is_prime:
            print(number)
print_primes(50)
