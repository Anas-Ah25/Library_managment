from repositories.book_repository import BookRepository
from models.book import Book

class BookService:
    def __init__(self):
        self.repository = BookRepository() # import the repository to take or pass data to it

    def add_book(self, data):
        required_fields = ["title", "author", "published_year", "genre", "ID"]
        for field in required_fields:
            if field not in data:
                return {"message": f"{field} is required."}, 400

        # ckeck if book already exist
        if self.repository.find_by_ID(data["ID"]):
            return {"message": "alredy exist"}, 400

        # new book 
        new_book = Book(**data)
        self.repository.add_book(new_book)
        return {"message": "Done"}, 201

    def get_books(self):
        return [book.__dict__ for book in self.repository.get_books()]
    def find_book(self, author=None, published_year=None, genre=None):
        books = self.repository.get_books() # all books
        books_list = []
        for book in books:
            if (
                (not author or book.author == author) and
                (not published_year or str(book.published_year) == str(published_year)) and
                (not genre or book.genre == genre)
            ):
                books_list.append(book.__dict__)  # object to a dictionary

        return books_list


    def delete_book_by_ID(self, ID):
        book = self.repository.find_by_ID(ID)
        if not book:
            return {"message": "not found"}, 404
        self.repository.delete_by_ID(ID)
        return {"message": f"Done, book {ID} is deleted"}, 200

    def update_book(self, ID, data):
        book = self.repository.update_book(ID, data)
        if not book:
            return {"message": "not found"}, 404
        return {"message": f"Done, book {ID} is updated"}, 200
