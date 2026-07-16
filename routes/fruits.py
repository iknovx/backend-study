from fastapi import APIRouter, HTTPException

from schemas.models import Fruits
from data.database import fruits


router = APIRouter(prefix="/fruits", tags=["fruits"])

with open("log/log.txt", "a") as log_file:
    log_file.write("Fetched all fruits\n")

# Get a list of fruits
@router.get("/", summary="Get a list of fruits")
def get_fruits():
    return fruits

# Get a fruit by ID
@router.get("/{fruit_id}", summary="Get a fruit by ID")
def find_fruit(fruit_id: int):
    for fruit in fruits:
        if fruit["id"] == fruit_id:
            return fruit
    raise HTTPException(status_code=404, detail="Fruit not found")

# Add a new fruit
@router.post("/", summary="Add a new fruit")
def add_fruit(fruit: Fruits):
    new_fruit = {
        "id": len(fruits) + 1,
        "name": fruit.name,
        "color": fruit.color,
        "price": fruit.price
    }

    fruits.append(new_fruit)
    return new_fruit    

# Update a fruit by ID
@router.put("/{fruit_id}", summary="Update a fruit by ID")
def update_fruit(fruit_id: int, fruit: Fruits):
    for i, f in enumerate(fruits):
        if f["id"] == fruit_id:
            fruits[i] = {
                "id": fruit_id,
                "name": fruit.name,
                "color": fruit.color,
                "price": fruit.price
            }
            return fruits[i]

    raise HTTPException(status_code=404, detail="Fruit not found")


# Delete a book by ID
@router.delete("/{fruit_id}", summary="Delete a fruit by ID")
def delete_fruit(fruit_id: int):
    for i, f in enumerate(fruits):
        if f["id"] == fruit_id:
            del fruits[i]
            return {"detail": "Fruit deleted"}

    raise HTTPException(status_code=404, detail="Fruit not found")

