from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = [{"id": 1, "name": "John", "age": 30, "student": True},
         {"id": 2, "name": "Jane", "age": 25, "student": False},
         {"id": 3, "name": "Doe", "age": 22, "student": True}]

class User(BaseModel):
    id: int
    name: str
    age: int
    student: bool


@app.get("/")
def home():
    return {"message": "API works"}


@app.post("/user")
def create_user(user: User):
    users.append(user.dict())
    return {"message": "User created", "user": user}


@app.get("/user")
def get_users():
    return users


@app.get("/user/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return {"message": "User not found"}


@app.get("/user/student/{is_student}")
def get_students(is_student: bool):
    students = [user for user in users if user["student"] == is_student]
    return {"students": students}

@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted"}
    return {"message": "User not found"}