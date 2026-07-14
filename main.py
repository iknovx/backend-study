from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()


books = [
    {"id": 1,
     "title": "1984", 
     "author": "George Orwell"},
    {"id": 2,
     "title": "To Kill a Mockingbird",
     "author": "Harper Lee"},
]


class Book(BaseModel):
    title: str
    author: str


@app.get("/")
def home():
    return {"message": "API works"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: Book):
    new_id = max((b["id"] for b in books), default=0) + 1
    new_book = book.dict()
    new_book["id"] = new_id
    books.append(new_book)
    return new_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(index)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)