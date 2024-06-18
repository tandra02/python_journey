'''Write a program that gets two inputs, numbers. The input numbers are the arguments of the below function. 
Create a function that gets two arguments, calculates the product of them and prints it, name the function however you like.
Call the function with the input numbers.'''

def product (x, y):
    return x*y

# Using list comprehension
[a, b] = [int(input()) for _ in range(2)]
print(product(a, b))