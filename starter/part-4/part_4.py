### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
def gather_book_info():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    rating = input("Enter the book's average rating: ")
    pages = input("Enter the number of pages: ")
    return {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }


### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
def gather_book_info_converted():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = int(input("Enter the year of publication: "))
    rating = float(input("Enter the book's average rating: "))
    pages = int(input("Enter the number of pages: "))
    return {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
def gather_book_info_safe():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    while True:
        try:
            year = int(input("Enter the year of publication: "))
            rating = float(input("Enter the book's average rating: "))
            pages = int(input("Enter the number of pages: "))
            return {
                "title": title,
                "author": author,
                "year": year,
                "rating": rating,
                "pages": pages
            }
        except ValueError:
            print("Please enter valid numerical values for year, rating, and pages.")



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def main_menu():
    library = []
    while True:
        print("\n1. Add a book")
        print("2. View library")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            book = gather_book_info_safe()
            library.append(book)
            print("Book added successfully.")
        elif choice == '2':
            for book in library:
                print(book)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
main_menu()  # Call this function to start the program.

