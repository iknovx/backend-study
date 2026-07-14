from fastapi import APIRouter, HTTPException

from schemas.models import Book
from data.database import books

router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", summary="Get a list of books")
def get_books():
    return books


@router.get("/{book_id}", summary="Get a book by ID")
def find_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.post("/", summary="Add a new book")
def add_book(book: Book):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author
    }

    books.append(new_book)
    return new_book


@router.put("/{book_id}", summary="Update a book by ID")
def update_book(book_id: int, book: Book):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            books[i] = {
                "id": book_id,
                "title": book.title,
                "author": book.author
            }
            return books[i]

    raise HTTPException(status_code=404, detail="Book not found")


@router.delete("/{book_id}", summary="Delete a book by ID")
def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b["id"] == book_id:
            del books[i]
            return {"detail": "Book deleted"}

    raise HTTPException(status_code=404, detail="Book not found")