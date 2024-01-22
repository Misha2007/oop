from book_store import Book
from book_store import Store

if __name__ == '__main__':
    book = Book("jaskdkhkd", "sdaldhasjd", 25, 20)
    book2 = Book("hello", "i", 23, 20)
    book3 = Book("hello", "i32", 24, 11)
    store = Store("jasdhkas", 10)
    store.add_book(book)
    store.add_book(book2)
    store.add_book(book3)
    #store.remove_book(book3)
    print(store.get_books_by_price())
    print(store.get_most_popular_book())