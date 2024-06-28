'''Create a function named find_most_recent_book that finds the most recently published book in a library catalog. The function should take the library catalog as an input parameter and return the title of the book that is the most recently published.'''

def find_most_recent_book(library_catalog):
    most_recent_title = None
    most_recent_year = -1
    # Iterating the list of dictionaries
    for book in library_catalog:
        # Checking for the most_recent key "year"
        if book["year"] > most_recent_year:
            # Assigning
            most_recent_year = book["year"]
            most_recent_title = book["title"]
    return most_recent_title


print(find_most_recent_book([{"title": "The Lion, the Witch and the Wardrobe", "year": 1950}, {"title": "A Tale of Two Cities", "year": 1859}, {"title": "Harry Potter and the Philosopher's Stone", "year": 1997}]))