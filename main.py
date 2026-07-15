
from fastapi import FastAPI

from routes.fruits import router as fruits_router
from routes.vegetables import router as vegetables_router
app = FastAPI(title="Shop API") # Main API for managing fruits and vegetables

# Include the fruits router
app.include_router(fruits_router) # Include the fruits router

app.include_router(vegetables_router) # Include the vegetables router

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)