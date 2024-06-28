'''Create a function named update_availability that allows you to update the availability status of a book in a library catalog. The function should take the library catalog, a title, and a new availability status as input parameters and update the availability status of the specified book in the catalog.'''

def update_availability(catalog, title, new_availability):
    if title in catalog:
        catalog[title]['available'] = new_availability
        return catalog[title]
    else:
        return "Book not found in the catalog"

# catalog = {
#     "1984": {"author": "George Orwell", "year": 1949, "available": False},
#     "Brave New World": {"author": "Aldous Huxley", "year": 1932, "available": True}
# }
# print(update_availability(catalog, "1984", True))

catalog = {
    "The Lion, the Witch and the Wardrobe": {"author": "C.S. Lewis", "year": 1950, "available": True}
}
print(update_availability(catalog, "The Lion, the Witch and the Wardrobe", False))

