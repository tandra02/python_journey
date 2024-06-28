'''Create a function named merge that receives two lists as arguments. The function merges the two lists into one sorted list and returns it.
For example the following arguments: merge([1, 4, 2], [2, 5, 9]) will return [1, 2, 2, 4, 5, 9]'''

def merge(lst1, lst2):
    # Combine the two lists
    combined_list = lst1 + lst2
    
    # Sort the combined list
    sorted_list = sorted(combined_list)
    
    return sorted_list

print(merge([100, 99, 88, 77], [1, 9, 2, 8, 3, 7, 5]))