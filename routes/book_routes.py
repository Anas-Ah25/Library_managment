from flask import request, jsonify
from services.book_service import BookService

def register_book_routes(app):
    book_service = BookService()

    #  ---------- get all books ----------
    @app.route("/books/all", methods=["GET"])
    def get_books():
        """
        Get a list of all books
        ---
        responses:
          200:
            description: A list of all books
            schema:
              type: array
              items:
                type: object
                properties:
                  ID:
                    type: string
                    description: The unique identifier of the book
                  title:
                    type: string
                    description: The title of the book
                  author:
                    type: string
                    description: The author of the book
                  published_year:
                    type: string
                    description: The year the book was published
                  genre:
                    type: string
                    description: The genre of the book
        """
        return jsonify(book_service.get_books())

    # -------- add book ----------
    @app.route("/books/add", methods=["POST"])
    def add_book():
        """
        Add a new book
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                ID:
                  type: string
                  example: "7"
                title:
                  type: string
                  example: "Anas's Life"
                author:
                  type: string
                  example: "A.A."
                published_year:
                  type: string
                  example: "2030"
                genre:
                  type: string
                  example: "Fiction"
        responses:
          201:
            description: Book added successfully
          400:
            description: Invalid input
        """
        data = request.get_json()
        response, status = book_service.add_book(data)
        return jsonify(response), status

    # -------- search books ----------
    @app.route("/books/search", methods=["GET"])
    def search_books():
        """
        Search for books
        ---
        parameters:
          - name: Author
            in: header
            type: string
            required: false
            description: The author of the book
          - name: Published-Year
            in: header
            type: string
            required: false
            description: The year the book was published
          - name: Genre
            in: header
            type: string
            required: false
            description: The genre of the book
        responses:
          200:
            description: A list of matching books
        """
        author = request.headers.get("Author")
        published_year = request.headers.get("Published-Year")
        genre = request.headers.get("Genre")
        return jsonify(book_service.find_book(author, published_year, genre))

    # -------- delete book ----------
    @app.route("/books/delete/<string:ID>", methods=["DELETE"])
    def delete_book(ID):
        """
        Delete a book by ID
        ---
        parameters:
          - name: ID
            in: path
            type: string
            required: true
            description: The unique identifier of the book
        responses:
          200:
            description: Book deleted successfully
          404:
            description: Book not found
        """
        response, status = book_service.delete_book_by_ID(ID)
        return jsonify(response), status

    # -------- update book ----------
    @app.route("/books/edit/<string:ID>", methods=["PUT"])
    def update_book(ID):
        """
        Update a book's details
        ---
        parameters:
          - name: ID
            in: path
            type: string
            required: true
            description: The unique identifier of the book
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                title:
                  type: string
                  example: "Updated Title"
                author:
                  type: string
                  example: "Updated Author"
                published_year:
                  type: string
                  example: "2025"
                genre:
                  type: string
                  example: "Updated Genre"
        responses:
          200:
            description: Book updated successfully
          404:
            description: Book not found
        """
        data = request.get_json()
        response, status = book_service.update_book(ID, data)
        return jsonify(response), status
