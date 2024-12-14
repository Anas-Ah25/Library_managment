class Book:
    def __init__(self, title, author, published_year, ID, genre=None):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.ID = ID
        self.genre = genre

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "published_year": self.published_year,
            "ID": self.ID,
            "genre": self.genre,
        }
