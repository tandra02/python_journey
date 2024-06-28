'''Each test case has one input - an odd whole number.
Your task is to print n - pyramid using *'''

n = int(input())
if n % 2 != 0:  # Ensure n is odd
    for i in range((n + 1) // 2):
        spaces = (n - (2 * i + 1)) // 2  # Calculate leading spaces
        stars = 2 * i + 1  # Calculate the number of stars
        print(' ' * spaces + '*' * stars + ' ' * spaces)
else:
    print("Input must be an odd integer.")