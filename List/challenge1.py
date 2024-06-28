'''Write a function named prod which gets a list of numbers as argument and returns the product of all the numbers in the list.
Reminder, product is the multiplication of all the numbers, for [1, 2, 3], return 6 = 1 * 2 * 3.'''

def prod(lst):
    # Write code here
    product = 1
    for i in lst:
        product *= i
    return product
print(prod([5, 3, 7, 1, 6, 2, 54, 123, -98, 32]))