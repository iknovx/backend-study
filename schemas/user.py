from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int
    student: bool