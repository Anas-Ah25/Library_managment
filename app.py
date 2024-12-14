from flask import Flask
from routes.book_routes import register_book_routes
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app) 

register_book_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
