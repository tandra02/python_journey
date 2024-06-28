# Given two lists of numbers nums1 and nums2.
# Create a list comprehension that takes in two lists of integers, nums1 and nums2, and returns a new list named total_nums containing the product of each combination of integers from the two lists.

nums1 = eval(input())
nums2 = eval(input())
total_nums = [one * two for one in nums1 for two in nums2]
print(total_nums)