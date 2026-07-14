from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()
class Book(BaseModel):
    title: str
    author: str
    

books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell"
    },

    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee"
    },

    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    },

    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen"
    }
]
# Get all books
@app.get(path="/books", tags=["books"], summary="Get a list of books")
def get_books():
    return books

# Get a book by ID
@app.get(path="/books/{book_id}", tags=["books"], summary="Get a book by ID")
def find_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Add a new book
@app.post(path="/books", tags=["books"], summary="Add a new book")
def add_book(book: Book):
    books.append({"id": len(books) + 1, 
                  "title": book.title, 
                  "author": book.author})
    return book

@app.put(path="/books/{book_id}", tags=["books"], summary="Update a book by ID")
def update_book(book_id: int, book: Book):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            books[i] = {"id": book_id, "title": book.title, "author": book.author}
            return books[i]
    raise HTTPException(status_code=404, detail="Book not found")
@app.delete(path="/books/{book_id}", tags=["books"], summary="Delete a book by ID")
def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            del books[i]
            return {"detail": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)