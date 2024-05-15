# Step 1 - Lists
my_authors = ["George Orwell", "Virginia Woolf", "James Joyce", "Toni Morrison", "Gabriel García Márquez", "Leo Tolstoy", "Haruki Murakami", "J.K. Rowling"]

# Add a new author to the end with the .append() method.
my_authors.append("F. Scott Fitzgerald")

# Remove an element in the list
my_authors.remove("James Joyce")

# Access an element by its index. (Remember indexes start at 0.)
print(my_authors[2])  # This should print "Toni Morrison" after removing James Joyce.

# Slice the list.
print(my_authors[1:4])  # This will print the slice from Virginia Woolf to Gabriel García Márquez.

# Step 2 - Tuples
my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickinson", "George Orwell", "Ray Bradbury")

# Step 3 - Sets
my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickinson", "George Orwell", "Ray Bradbury"}

# Add a new author to your set.
my_author_set.add("J.R.R. Tolkien")

# Try adding the same author again, and be sure to print your set.
my_author_set.add("J.R.R. Tolkien")
print(my_author_set)  # Notice that adding "J.R.R. Tolkien" again does not change the set.

# Step 4 - For Loops
# Loop through list
for author in my_authors:
    print(author)

# Loop through tuple
for author in my_author_tuple:
    print(author)

# Loop through set
for author in my_author_set:
    print(author)