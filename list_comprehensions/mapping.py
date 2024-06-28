# Given a list of number nums, Assuming each element is x, calculate a new list where each element is calculated with the following equation: x3+2*x2+5
# Store the new list in a variable named new_nums.

nums = eval(input())
new_nums = [x ** 3 + 2 * x ** 2 +  5 for x in nums]
print(f"New nums = {new_nums}")