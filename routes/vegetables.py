from fastapi import APIRouter, HTTPException
from schemas.models import Vegetables
from data.database import vegetables

router = APIRouter(prefix="/vegetables", tags=["vegetables"])

# Get a list of vegetables
@router.get("/", summary="Get a list of vegetables")
def get_vegetables():
    return vegetables

# Get a vegetable by ID
@router.get("/{vegetable_id}", summary="Get a vegetable by ID")
def find_vegetable(vegetable_id: int):
    for vegetable in vegetables:
        if vegetable["id"] == vegetable_id:
            return vegetable
    raise HTTPException(status_code=404, detail="Vegetable not found")


# Add a new vegetable
@router.post("/", summary="Add a new vegetable")
def add_vegetable(vegetable: Vegetables):
    new_vegetable = {
        "id": len(vegetables) + 1,
        "name": vegetable.name,
        "color": vegetable.color,
        "price": vegetable.price
    }

    vegetables.append(new_vegetable)
    return new_vegetable

# Update a vegetable by ID
@router.put("/{vegetable_id}", summary="Update a vegetable by ID")
def update_vegetable(vegetable_id: int, vegetable: Vegetables):
    for i, v in enumerate(vegetables):
        if v["id"] == vegetable_id:
            vegetables[i] = {
                "id": vegetable_id,
                "name": vegetable.name,
                "color": vegetable.color,
                "price": vegetable.price
            }
            return vegetables[i]

    raise HTTPException(status_code=404, detail="Vegetable not found")

# Delete a vegetable by ID
@router.delete("/{vegetable_id}", summary="Delete a vegetable by ID")
def delete_vegetable(vegetable_id: int):
    for i, v in enumerate(vegetables):
        if v["id"] == vegetable_id:
            del vegetables[i]
            return {"detail": "Vegetable deleted"}

    raise HTTPException(status_code=404, detail="Vegetable not found")