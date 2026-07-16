from fastapi import APIRouter, HTTPException
from schemas.models import Sodas
from data.database import sodas
router = APIRouter(prefix="/soda", tags=["soda"])

@router.get("/", summary="Get a list of sodas")
def get_sodas():
    return sodas

@router.get("/{soda_id}", summary="Get a soda by ID")
def find_soda(soda_id: int):
    for soda in sodas:
        if soda["id"] == soda_id:
            return soda
    raise HTTPException(status_code=404, detail="Soda not found")

@router.post("/", summary="Add a new soda")
def add_soda(soda: Sodas):
    new_soda = {
        "id": len(sodas) + 1,
        "name": soda.name,
        "brand": soda.brand,
        "price": soda.price
    }

    sodas.append(new_soda)
    return new_soda

@router.put("/{soda_id}", summary="Update a soda by ID")
def update_soda(soda_id: int, soda: Sodas):
    for index, existing_soda in enumerate(sodas):
        if existing_soda["id"] == soda_id:
            sodas[index] = {
                "id": soda_id,
                "name": soda.name,
                "brand": soda.brand,
                "price": soda.price
            }
            return sodas[index]
    raise HTTPException(status_code=404, detail="Soda not found")

@router.delete("/{soda_id}", summary="Delete a soda by ID")
def delete_soda(soda_id: int):
    for index, existing_soda in enumerate(sodas):
        if existing_soda["id"] == soda_id:
            del sodas[index]
            return {"detail": "Soda deleted"}
    raise HTTPException(status_code=404, detail="Soda not found")
