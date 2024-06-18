'''Write a program that gets one input, a number. The input number indicates how many times to execute the below function. 

Create a function that calculates the sum of all of the numbers between 1 and 10000 (including) and prints it, name the function however you like.'''

def sum_numbers():
    total = 0
    for i in range(1, 10001):
        total += i
    return total

user_number = int(input())
for i in range(user_number):
    result = sum_numbers()
    print(result)