# Dictionary for book information
my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Function to format book information
def format_book_info(book):
    return (f"Title: {book['title']}\n"
            f"Author: {book['author']}\n"
            f"Year Published: {book['year']}\n"
            f"Average Rating: {book['rating']}\n"
            f"Pages: {book['pages']}")

# Print formatted book information
print(format_book_info(my_book))

# Functions to return individual pieces of information from the book
def get_title(book):
    return book['title']

def get_author(book):
    return book['author']

def get_publication_year(book):
    return book['year']

def get_rating(book):
    return book['rating']

def get_page_count(book):
    return book['pages']

# Test one of the functions
print(get_title(my_book))  # Output should be "The Hunger Games"

# Additional functions for expanding a home library app
def add_book(library, book):
    library.append(book)

def remove_book(library, title):
    for book in library:
        if book['title'] == title:
            library.remove(book)
            return f"Removed book titled '{title}'"
    return "Book not found"

def search_books_by_author(library, author_name):
    return [book for book in library if book['author'].lower() == author_name.lower()]

# Example usage of new functions
library = [my_book]
new_book = {
    "title": "Catching Fire",
    "author": "Suzanne Collins",
    "year": 2009,
    "rating": 4.29,
    "pages": 391
}
add_book(library, new_book)
print(remove_book(library, "Catching Fire"))  # Output should confirm removal
print(search_books_by_author(library, "Suzanne Collins"))  # Output should list books by Suzanne Collins
