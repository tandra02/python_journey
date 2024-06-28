'''Write a function named reverse which gets a list of numbers as argument and returns the reversed list.
For example, for [1, 2, 3], the expected output is [3, 2, 1].'''

def reverse(lst):
    # Write code here
    final = lst[::-1]
    return final

print(reverse([3, 5, 7, 1, -4, 98]))