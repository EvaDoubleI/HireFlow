from fastapi import FastAPI

app = FastAPI(title="HireFlow app")

from app.api.routers import include_routers

include_routers(app)

@app.get("/")
def root():
    return {"message": "Active"}
