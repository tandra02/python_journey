'''You are given a dictionary, your task is to access all the items in the dictionary and print its value, keep the dictionary values order!'''

book = {
    "title": "Python for Beginners",
    "author": "Alice Smith",
    "year": 2022,
    "pages": 200,
    "genre": "Programming",
    "publisher": "Tech Books Inc."
}
for value in book.values():
    print(value)