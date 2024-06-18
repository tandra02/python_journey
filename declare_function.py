'''Write a program that gets one input, a number. The input number indicates how many times to execute the below function. 
Create a function that calculates the sum of all of the numbers between 1 and 10000 (including) and prints it, name the function however you like.'''

def sum_all_numbers():
    total = sum(range(1, 10001))
    print(total)

# Get the number of times to execute the function from user input
n = int(input())

# Execute the function 'n' times
for _ in range(n):
    sum_all_numbers()