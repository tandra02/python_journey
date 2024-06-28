# Create a list comprehension that takes in nums and returns a new list named nums2 that stores integers after dividing them by 3 if they are multiples of 3.

nums = eval(input())  # Don't change this line
nums2 = [x // 3 for x in nums if x % 3 == 0]
print(nums2)