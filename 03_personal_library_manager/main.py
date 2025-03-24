import json

LIBRARY_FILE = "library.json"

def load_library():
    """Load library data from a file"""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a new book to the library"""
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the publication year of the book: ")
    genre = input("Enter the genre of the book: ")
    is_read = input("Have you read it? (yes/no)").strip().lower() == "yes"
    book = {
        "title": title, 
        "author": author, 
        "year": year, 
        "genre": genre,
        "is_read": is_read
        }
    library.append(book)
    save_library(library)
    print(f"Book '{title}' added successfully!\n")

def remove_book(library):
    """Remove a book from library by title"""
    title = input("Enter the title of the book to remove: ").strip()

    for book in library:
      if book["title"].lower() == title.lower():
        library.remove(book)
        save_library(library)
        print(f"Book '{title}' removed successfully!\n")
        return
    print("Book not found.\n")

def search_books(library):
    """Search for books by title, author, or genre."""
    query = input("Enter title, author or genre to search: ").strip().lower()
    results = [book for book in library if query in book['title'].lower() or query in book['author'].lower() or query in book['genre'].lower()]

    if results:
        print("Search Results:")
        for book in results:
            print(f"- {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['is_read'] else 'No'}")
    else:
        print("No books found matching the search criteria.\n")

def list_books(library):
    """List all books in the library."""
    if library:
        print("\nBooks in the Library:")
        for book in library:
            print(f"- {book['title']} by {book['author']} ({book['year']}) - Genre: {book['genre']} - Read: {'Yes' if book['is_read'] else 'No'}")
    else:
        print("The library is empty.\n")

def show_stats(library):
    """Show library statistics."""
    total_books = len(library)
    read_books = sum(1 for book in library if book['is_read'])
    unread_books = total_books - read_books
    print(f"\nTotal Books: {total_books}")
    print(f"Read Books: {read_books}")
    print(f"Unread Books: {unread_books}\n")
                


def main():
    """Main menu for the Personal Library Manager."""
    library = load_library()

    while True:
        print("\nPersonal Library Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. List All Books")
        print("5. Show Library Statistics")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            list_books(library)
        elif choice == "5":
            show_stats(library)            
        elif choice == "6":
            print("Goodbye!")
            break    
        else:
            print("Invalid option, please try again.\n")

if __name__ == "__main__":
    main()      

