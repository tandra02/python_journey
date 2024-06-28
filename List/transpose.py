def transpose(lst):
    if not lst:
        return []

    # Number of rows and columns in the original list
    num_rows = len(lst)
    num_cols = len(lst[0])

    # Create a new list with empty rows for transposed elements
    transposed = []
    for col in range(num_cols):
        new_row = []
        for row in range(num_rows):
            new_row.append(lst[row][col])
        transposed.append(new_row)

    return transposed

list_value = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(list_value))

