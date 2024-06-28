# Create a list comprehension that takes in a list of strings strings and returns a new list named pairs containing all the pairs of strings that share no common letters.
# The result should be ordered by the occurrence of the words in the given list (by indexes).

strings = eval(input())
pairs = [(x, y) for i, x in enumerate(strings) for j, y in enumerate(strings) if i < j and not set(x) & set(y)]
print(pairs)