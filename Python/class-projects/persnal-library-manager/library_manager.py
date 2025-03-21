# Add book
def add_book(library):
    book_title = input("Enter the book title: ")
    book_author = input("Enter the author: ")
    publication_year = int(input("Enter the publication year: "))
    book_genre = input("Enter the genre: ")
    book_read = input("Have you read this book? (yes/no): ").strip().lower()
    if book_read == 'yes':
        book_read = True
    elif book_read == 'no':
        book_read = False


    book = {
        "title": book_title,
        "author": book_author,
        "year": publication_year,
        "genre": book_genre,
        "read": book_read
        }
    
    library.append(book)

    print("Book added successfully!")
# remove books
def remove_books (library):
    book_title = input("Enter the title of the book to remove: ") 

    for book in library:
        if book["title"] == book_title:
            library.remove(book)
            print(f"{book_title} removed successfully!")
            return
        
    print("Book not found in library!")



# Search book
def search_books(library):
    print("search by:")
    print("1. Title")
    print("2. Author")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_title = input("Enter the title: ").strip().lower()
        book_found = [book for book in library if book["title"].strip().lower() == book_title]

    elif choice == "2":
        book_author = input("Enter the author: ").strip().lower()
        book_found = [book for book in library if book["author"].strip().lower() == book_author]

    else:
        print("Invalid Choice!")

    
    if book_found:
        print("Matching Books:")
        for index, book in enumerate(book_found, start=1):
            read_status = "Read" if book["read"] else "Not Read"
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found!")



def library_manager():
    library = []
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        # Add a Book
        if choice == "1":
            print("You selected: Add a book")
            add_book(library)
            
        # Remove a Book
        elif choice == "2":
            print("You selected: Remove a book")
            remove_books(library)

        # Search a book
        elif choice == "3":
            print("You selected: Search for a book")
            search_books(library)

        # Display Books
        elif choice == "4":
            if not library:
                print("Your Library is empty!")
            else:
                print("\nYour Library:")
                for index, book in enumerate(library, start=1):
                    read_status = "Read" if book["read"] else "Unread"
                    
                    print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")


        # Display Statistics
        elif choice == "5":
            total_books = len(library)
            if total_books > 0:
                read_books = sum(1 for book in library if book["read"])
                read_percentage = (read_books / total_books) * 100
                print(f"Total books: {total_books}")
                print(f"Percentage read: {read_percentage:.1f}%")  
            else:
                print("Your Library is empty!")


        # Exit
        elif choice == "6":
            print("Exiting the program.")
            break

        
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

library_manager()