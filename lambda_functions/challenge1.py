# Write a lambda function that receives a list of tuples that each tuple contains two integers. The lambda returns a new list containing only the tuples where the first integer is greater than the second integer.
# Assign the lambda function to a variable named first_bigger.

tuples = [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]
first_bigger = lambda tuples: list(filter(lambda t: t[0] > t[1], tuples))
filtered_tuples = first_bigger(tuples)
print(filtered_tuples)