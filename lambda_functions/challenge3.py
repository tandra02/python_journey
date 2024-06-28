# Write a lambda function that receives a list of integers and returns the median value of the list.
# The median is the middle value in a sorted list, or the average of the two middle values if the list has an even number of elements


median = lambda x: (sorted(x)[len(x) // 2] if len(x) % 2 != 0 else (sorted(x)[len(x) // 2 - 1] + sorted(x)[len(x) // 2]) / 2)
print(median([15, 7, 4, 19, 3, 8]))