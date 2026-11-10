# "Borrowed" is False from the start. True = borrowed, False = returned/available
Books = [
    {"Title": "Making It Big:", "Author": " Femi Otedola", "Borrowed": False},
    {"Title": "Rich Dad Poor Dad ", "Author": "Robert Kiyosaki (co-authored with Sharon Lechter).", "Borrowed": False},
    {"Title": "The Seven Habits of Highly Effective People", "Author": "Stephen Covey", "Borrowed": False},
    {"Title": "She Stoops to Conquer", "Author": "Oliver Goldsmith", "Borrowed": False},
    {"Title": "A Raisin in the Sun", "Author": "Lorraine Hansberry", "Borrowed": False},
    {"Title": "The Power of Now", "Author": "Eckhart Tolle", "Borrowed": False},
]

# All accounts (libarians AND users): {username: {"Password": ..., "Role": ...}}
Accounts = {
    "admin": {"Password": "1234", "Role": "libarian"},
}

# LIBARIAN (menu shown after a libarian logs in)
def Libarian(name):

    def add_book(book_title, book_author):
        Books.append({"Title": book_title, "Author": book_author, "Borrowed": False})
        print(f"Successfully added '{book_title}'")

    def remove_book(book_title):
        for book in Books:
            if book_title.lower() == book["Title"].lower():
                Books.remove(book)
                print(f"Successfully removed '{book_title}'")
                return
        print("Book not found")

    print(f"\nWelcome Libarian {name}")
    while True:
        option = input("\nWhat would you like to do: \n1. Add a Book \n2. Remove a Book \n3. Logout \n: ")
        if option == "1":
            title = input("Enter Book title: ")
            author = input("Enter Book author: ")
            add_book(title, author)
        elif option == "2":
            title = input("Title of the book you want to remove: ")
            remove_book(title)
        elif option == "3":
            print(f"Goodbye {name}")
            break
        else:
            print("Invalid input")


# USER (menu shown after a user logs in)
def User(name):

    def view_books():
        if len(Books) == 0:
            print("No books in the library")
            return
        print("\n--- ALL BOOKS ---")
        for number, book in enumerate(Books, start=1):
            status = "Borrowed" if book["Borrowed"] else "Available"
            print(f"{number}. {book['Title']} by {book['Author']} [{status}]")

    def search_book(search_word):
        found = False
        for book in Books:
            if search_word.lower() in str(book["Title"]).lower() or search_word.lower() in str(book["Author"]).lower():
                status = "Borrowed" if book["Borrowed"] else "Available"
                print(f"- {book['Title']} by {book['Author']} [{status}]")
                found = True
        if not found:
            print("No book found")

    def borrow_book(book_title):
        for book in Books:
            if book_title.lower() == str(book["Title"]).lower():
                if book["Borrowed"]:
                    print("Sorry, this book has already been borrowed")
                else:
                    book["Borrowed"] = True
                    print(f"You have borrowed '{book['Title']}'")
                return
        print("Book not found")

    def return_book(book_title):
        for book in Books:
            if book_title.lower() == str(book["Title"]).lower():
                if book["Borrowed"]:
                    book["Borrowed"] = False
                    print(f"You have returned '{book['Title']}'. Thank you!")
                else:
                    print("This book was not borrowed")
                return
        print("Book not found")

    print(f"\nWelcome {name}")
    while True:
        option = input(
            "\n1. View all books \n2. Search for a book \n3. Borrow a book "
            "\n4. Return a book \n5. Exit \n: "
        )
        if option == "1":
            view_books()
        elif option == "2":
            keyword = input("Enter title or author to search: ")
            search_book(keyword)
        elif option == "3":
            title = input("Title of the book you want to borrow: ")
            borrow_book(title)
        elif option == "4":
            title = input("Title of the book you want to return: ")
            return_book(title)
        elif option == "5":
            print(f"Goodbye {name}")
            break
        else:
            print("Invalid input")

def start():

    def signup(new_username, new_password, new_role):
        if new_username in Accounts:
            print("Username already taken. Try another one.")
            return
        Accounts[new_username] = {"Password": new_password, "Role": new_role}
        print(f"Signup successful as a {new_role}! You can now login.")

    def login(user_name, user_password):
        if user_name in Accounts and Accounts[user_name]["Password"] == user_password:
            print("Login Successful")
            return Accounts[user_name]["Role"]
        print("Wrong username or password")
        return None

    while True:
        print("\nWELCOME to Himmaqulate Library")
        choice = input("1. Signup \n2. Login \n3. Exit \n: ")

        if choice == "1":
            username = input("Choose a Username: ")
            role_choice = input("Sign up as: \n1. Libarian \n2. User \n: ")
            if role_choice == "1":
                role = "libarian"
            elif role_choice == "2":
                role = "user"
            else:
                print("Invalid input, Try again!")
                continue
            password = input("Choose a Password: ")
            signup(username, password, role)

        elif choice == "2":
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            role = login(username, password)
            if role == "libarian":
                Libarian(username)
            elif role == "user":
                User(username)

        elif choice == "3":
            print("Thank you for visiting School 2 Library")
            break
        else:
            print("Invalid input, Try again!")


start()