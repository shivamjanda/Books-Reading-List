# ------------------------------------------------------------------------------------------------------------------------------------
# Name: Shivam Janda
# Date: October, 14, 2022
# Program: sysa-3204
# Description: Store and retrieve information related to a user's reading list. Options include: adding a new book,
#              listing all the books, marking a book as read, deleting a book and quiting the program.
# ------------------------------------------------------------------------------------------------------------------------------------
import datetime

from utils import database

USER_CHOICE = """Enter:
-> 'a' to add a new book
-> 'l' to list all books
-> 'r' to mark a book as read
-> 'd' to delete a book
-> 'q' to quit

Your choice: """


def prompt_add_book():
    while True:
        name = input("Enter the new book name: ")
        author = input("Enter the new book author: ")
        year = input("Enter the year of publication: ")

        # validate book name
        if name == "":
            print("Failed to add book to database, Please enter a book title\n")
            return

        # validate book name
        if author == "":
            print("Failed to add book to database, Please enter an author\n")
            return

        # validate publication year
        try:
            # cast to integer
            year = int(year)

            # before the year 1000
            if year < 1000:
                print("Sorry, the oldest book that can be recorded is from the year 1000\n")
                return

            # in the future
            if year > datetime.date.today().year:
                print("Sorry, we cannot store book that have not been published yet\n")
                return

        # invalid number
        except ValueError:
            print("Please enter a valid digit for the year of publication\n")
            return

        # if all valid break from loop
        break

    database.add_book(name, author, year)
    print(f"Successfully added: {name} by {author}, {year}, to your database\n")


def list_books():
    books = database.get_all_books()
    if len(books) == 0:
        print('There are no books in your database\n')
        return

    for book in books:
        read = "YES" if book.get('read') == '1' else "NO"
        print(f"{book['title']} by {book['author']}, {book['year']} — Read: {read}")


def read_book():
    title = input('Enter the name of the book you just finished reading: ')
    print(database.mark_book_as_read(title))


def delete_book():
    title = input('Enter the name of the book you wish to delete: ')
    print(database.delete_book(title))


action = {
    'a': prompt_add_book,
    'l': list_books,
    'r': read_book,
    'd': delete_book
}


def menu():
    while (selection := input(USER_CHOICE)) != "q":
        if selection in action:
            action[selection]()
        else:
            print("Unknown command. Please try again.\n")


if __name__ == "__main__":
    database.create_book_table()
    menu()
