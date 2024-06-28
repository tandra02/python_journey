'''Create a function named add_book that adds books to a library catalog represented as a dictionary. The function should take the title (the key), author, and publication year as input parameters and add a new book entry to the catalog with initial availability marked as "available."
catalog is the library catalog dictionary.
title is the title of the book.
author is the author of the book.
year is the publication year of the book.
After running the function with these examples, the catalog dictionary should include these two books with their details and an initial availability status.'''

def add_book(catalog, title, author, year):

    catalog[title] = {
        "author": author,
        "year": year,
        "available": True
    }
    return catalog

catalog = {}
print(add_book(catalog, "1984", "George Orwell", 1949))
print(add_book(catalog, "Brave New World", "Aldous Huxley", 1932))