from pydantic import BaseModel

# Fruits model
class Fruits(BaseModel):
   name: str
   color: str
   price: float

class Vegetables(BaseModel):
   name: str
   color: str
   price: float