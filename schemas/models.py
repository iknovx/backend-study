from pydantic import BaseModel

# Book model
class Book(BaseModel):
   title: str
   author: str
   year: int

