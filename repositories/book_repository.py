import json
from models.book import Book

'''  The main approach here with repository is that layer deal directly with the data, which is 
     books model (using the data json but in normal we was going to be using database), but the flow is the same
'''
class BookRepository:
    # ------- Constructor -------
    def __init__(self, data_file="data.json"):
        self.data_file = data_file
        self.books = self.load_books()

    # ------- loading the data -------
    def load_books(self):
        try:
            with open(self.data_file, "r") as file:
                return [Book(**book) for book in json.load(file)]
        except FileNotFoundError:
            return []

    # ------- saving the data -------
    def save_books(self):
        with open(self.data_file, "w") as file:
            books_list = []
            for book in self.books:
                books_list.append(book.__dict__)
            json.dump(books_list, file) 

    # ------- searching, adding, updating , get and delete books -------
    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def get_books(self):
        return self.books

    def find_by_ID(self, ID):
        for book in self.books:
            if book.ID == ID:
                return book
        return None

    def delete_by_ID(self, ID):
        for book in self.books:
            if book.ID == ID:
                self.books.remove(book)
                break
        self.save_books()

    def update_book(self, ID, data):
        book = self.find_by_ID(ID) # search by the book id
        if book:
            for key, value in data.items():
                setattr(book, key, value) #  set the value of the book (which is an object)
            self.save_books()
            return book
        return None
