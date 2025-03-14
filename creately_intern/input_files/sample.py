import os

# Define a class to represent a Book
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


# Function to read book data from a file
def read_books(file_name):
    books = []
    if not os.path.exists(file_name):
        print("File not found!")
        return books

    with open(file_name, 'r') as file:
        for line in file:
            title, author, year = line.strip().split(',')
            books.append(Book(title, author, int(year)))
    return books


# Function to write book data to a file
def write_books(file_name, books):
    with open(file_name, 'w') as file:
        for book in books:
            file.write(f"{book.title},{book.author},{book.year}\n")


# Function to display all books
def display_books(books):
    if not books:
        print("No books to display.")
        return

    for book in books:
        book.display()
        print("-" * 30)


# Main function
def main():
    file_name = 'books.txt'

    # Sample list of books to write to the file
    books = [
        Book("1984", "George Orwell", 1949),
        Book("To Kill a Mockingbird", "Harper Lee", 1960),
        Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
        Book("Moby-Dick", "Herman Melville", 1851)
    ]
    
    write_books(file_name, books)
    print("Books written to file successfully!\n")

    # Read the books from the file and display them
    read_books_list = read_books(file_name)
    print("Books read from file:\n")
    display_books(read_books_list)


if __name__ == "__main__":
    main()
