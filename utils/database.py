import csv

books_file = 'books.csv'


def create_book_table():
    try:
        with open(books_file, 'x') as file:
            file.close()

        with open(books_file, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'author', 'year', 'read'])
            writer.writeheader()

    except FileExistsError:
        return


def get_all_books():
    with open(books_file, 'r') as file:
        reader = csv.DictReader(file)
        lines = [line for line in reader]

    return [{key: value for key, value in line.items()} for line in lines]


def add_book(name, author, year):
    with open(books_file, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'author', 'year', 'read'])

        writer.writerows([
            {
                'title': name,
                'author': author,
                'year': year,
                'read': 0
            }
        ])


def _save_all_books(books):
    with open(books_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'author', 'year', 'read'])
        writer.writeheader()
        writer.writerows(books)


def mark_book_as_read(title):
    books = get_all_books()
    for book in books:
        if book['title'] == title:
            book['read'] = 1
            _save_all_books(books)
            return f"Successfully marked {title} as read\n"

    else:
        return f"Could not mark {title} as read\n"


def delete_book(title):
    books = get_all_books()
    books = [book for book in books if book['title'] != title]
    _save_all_books(books)
    return f"Successfully removed all occurrences of {title} from your database"
