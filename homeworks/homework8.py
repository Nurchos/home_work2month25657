import sqlite3


def connect_db():
    return sqlite3.connect("books.db")


def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_books():
    conn = connect_db()
    cursor = conn.cursor()

    books = [
        ("1984", "George Orwell", 1949, "Dystopian", 328, 5),
        ("War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 3),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 7),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 400, 10),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 180, 4),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Classic", 281, 6),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Classic", 214, 2),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Philosophical", 671, 5),
        ("Moby Dick", "Herman Melville", 1851, "Adventure", 635, 3),
        ("Brave New World", "Aldous Huxley", 1932, "Dystopian", 311, 8)
    ]

    cursor.executemany("""
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    conn.commit()
    conn.close()


def get_all_books():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    for book in books:
        print(book)

    conn.close()


def get_books_by_author(author):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books WHERE author = ?", (author,))
    books = cursor.fetchall()

    for book in books:
        print(book)

    conn.close()


def delete_book_by_id(book_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    insert_books()

    print("\n📚 Все книги:")
    get_all_books()

    print("\n🔍 Книги автора George Orwell:")
    get_books_by_author("George Orwell")

    print("\n❌ Удаляем книгу с id = 1")
    delete_book_by_id(1)

    print("\n📚 После удаления:")
    get_all_books()
