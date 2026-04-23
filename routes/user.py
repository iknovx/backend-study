from fastapi import APIRouter
from schemas.user import User
from models.user import users

router = APIRouter()

@router.post("/user")
def create_user(user: User):
    users.append(user.dict())
    return {"message": "User created", "user": user}


@router.get("/user")
def get_users():
    return users


@router.get("/user/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return {"message": "User not found"}


@router.get("/user/student/{is_student}")
def get_students(is_student: bool):
    return [u for u in users if u["student"] == is_student]


@router.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return {"message": "User deleted"}
    return {"message": "User not found"}