from pydantic import BaseModel, Field, EmailStr, ConfigDict
from fastapi import FastAPI
app = FastAPI()

data = {
    "email": "user@example.com",
    "age": 30,
    "bio": "Software Developer"
}
data_without_age = {
    "email": "user@example.com",
    "bio": "Software Developer",
    "hobby": "Coding",
    "gender": "Male"
}
class User(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10)
    model_config = ConfigDict(
        extra="forbid"
    )
users = []

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"users": users}

class UserAge(User):
    age: int | None = Field(ge=0, le=120)

user = User(**data_without_age)
user1 = UserAge(**data)
print(repr(user))
print(repr(user1))

