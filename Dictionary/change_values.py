'''You are given a stock dictionary, your task:

Update the stock of apples to 12.
Reduce the stock of cherries by 2.
Increase the stock of dates by 3.
Decrease the stock of bananas by 5.'''

# The stock dictionary
stock = {
    "apple": 10,
    "banana": 15,
    "cherry": 5,
    "date": 8
}

# Your code here:
stock.update({"apple": 12})
stock["cherry"] = 3
stock["date"] = 11
stock["banana"] = 10
# Don't change below this line
print("Updated Stock:", stock)