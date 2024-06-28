'''Create a function named search_book that allows you to search for a book in a library catalog by its title. The function should take the library catalog and a title as input and return the book's details (title, author, publication year, and availability) if the book is found. If the book is not in the catalog, the function should return a message indicating that the book is not found.'''

def search_book(catalog, title):
    if title in catalog:
        return catalog[title]
    else:
        return "Book not found in the catalog"

catalog = {
    "1984": {"author": "George Orwell", "year": 1949, "available": True},
    "Brave New World": {"author": "Aldous Huxley", "year": 1932, "available": True}
}
print(search_book(catalog, "The Catcher in the Rye"))

# catalog = {
#     "1984": {"author": "George Orwell", "year": 1949, "available": True},
#     "Brave New World": {"author": "Aldous Huxley", "year": 1932, "available": True}
# }
# print(search_book(catalog, "1984"))
