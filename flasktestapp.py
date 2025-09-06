from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory "database"
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"}
]

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/books", methods=["POST"])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)