from fastapi import FastAPI
from routes import user

app = FastAPI()

app.include_router(user.router)


@app.get("/")
def home():
    return {"message": "API works"}