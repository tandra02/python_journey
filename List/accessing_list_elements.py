'''Create a function named values that receives a list as an argument and prints all of the items in the list one after the other.'''

def values(lst):
    # Write code here
    for item in range(len(lst)):
        print(lst[item])

values([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3 ,-4, -5, -6, -7, -8, -9, -10, -11, -12, 1023, -13])