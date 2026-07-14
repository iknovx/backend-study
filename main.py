
from fastapi import FastAPI
from routes.books import router as books_router

app = FastAPI(title="Books API")

app.include_router(books_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)