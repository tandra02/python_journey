'''You're given a dictionary representing a collection of words and their meanings. Your task is to write a function named find_meaning that checks if a given word exists in the dictionary.'''

# The dictionary of words and their meanings
word_meanings = {
    "apple": "a fruit",
    "book": "a written or printed work",
    "car": "a motor vehicle with four wheels",
    "dog": "a domesticated mammal"
}

# Your code here
def find_meaning(word):
    return word in word_meanings
# Don't change below this line
print("Does 'book' exist in the dictionary?", find_meaning("book"))
print("Does 'cat' exist in the dictionary?", find_meaning("cat"))
print("Does 'dog' exist in the dictionary?", find_meaning("dog"))
