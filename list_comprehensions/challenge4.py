# Create a list comprehension that takes in a list of integers, nums, and returns a new list named divisible containing only the integers that are divisible by the sum of their digits.

nums = eval(input())
divisible = [x for x in nums if x % sum(int(digit) for digit in str(x)) == 0]
print(divisible)