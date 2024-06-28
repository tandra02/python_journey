# Given a list of number nums, calculate a new list where only the even numbers exists.
# Store the new list in a variable named even_nums.

nums = eval(input())
even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)