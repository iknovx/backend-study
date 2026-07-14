
from fastapi import FastAPI
from routes.books import router as books_router

app = FastAPI(title="Books API") # Main API for managing books

app.include_router(books_router) # Include the books router

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)