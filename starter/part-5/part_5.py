### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
# Step 1 - Store data in a .txt
def add_book_to_file(book, filename='library.txt'):
    with open(filename, 'a') as file:
        file.write(f"{book['title']},{book['author']},{book['year']},{book['rating']},{book['pages']}\n")

# Step 2 - Read data from a .txt
def display_library(filename='library.txt'):
    try:
        with open(filename, 'r') as file:
            for line in file:
                title, author, year, rating, pages = line.strip().split(',')
                book = {
                    "title": title,
                    "author": author,
                    "year": int(year),
                    "rating": float(rating),
                    "pages": int(pages)
                }
                print(format_book_info(book))
    except FileNotFoundError:
        print("No library data found. Please add books to the library first.")

# Step 3 - if __name__ == "__main__":
if __name__ == "__main__":
    main_menu()

# Step 4 - Expand and refactor
# The above implementation already includes functionalities such as adding a book, displaying the library, and error handling.
# It is modular and expandable for future enhancements like searching and removing books by different criteria.