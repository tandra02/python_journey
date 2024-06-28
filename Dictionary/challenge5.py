'''Create a function named calculate_total_value that calculates the total value of items in a dictionary, where the keys represent item names, and the values represent their prices. The function should take this dictionary as input and return the total value.'''

def calculate_total_value(items_dict):
    # Write code here
    sum_of_values = 0
    for item in items_dict.values():
        sum_of_values += item
    return sum_of_values

print(calculate_total_value({"item1": 2.5, "item2": 3, "item3": 1.75}))