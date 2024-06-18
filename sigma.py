'''Write a function named sigma with one argument that represents a number n.

The function will return the sum of all the numbers from 1 to n (including).

For example, for sigma(5), the function will return 15, because 15 = 1 + 2 + 3 + 4 + 5.'''

def sigma(n):
    n_sum = 0
    for i in range(1, n+1):
        n_sum += i
    print(n_sum)

value = int(input())
sigma(value)