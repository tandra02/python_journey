# Write a lambda function that receives a list of tuples that each tuple contains two integers. The lambda returns a new list containing only the tuples where the first integer is greater than the second integer.
# Assign the lambda function to a variable named first_bigger.

def first_bigger(tuples):
    # Define the lambda function to check if the first element is greater than the second
    first_bigger_check = lambda i: i[0] > i[1]

    # Use the filter function with the lambda function
    filtered_tuples = filter(first_bigger_check, tuples)

    # Convert the filter object to a list and return it
    return list(filtered_tuples)

# Example usage
tuples = [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]
result = first_bigger(tuples)
print(f"first_bigger({tuples}) = {result}")
