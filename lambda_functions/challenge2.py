# Write a lambda function that receives a list of tuples, where each tuple contains three integers. The lambda returns a new list containing only the sum of the tuples that the sum of the integers are greater than 20.
# Assign the lambda function to a variable named sum_bigger.

tuples = [(5, 15, 5), (10, 10, 10), (20, 0, 5), (2, 4, 6)]
sum_bigger = lambda tuples : list(filter(lambda i: sum(i) > 20, tuples))
filtered_sum = sum_bigger(tuples)
sums = [sum(t) for t in filtered_sum]
print(sums)