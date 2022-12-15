from fastapi import FastAPI

from routes import routers
from utils.mongodb import database_interface

app = FastAPI()

for router in routers:
    app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Storage Interface service alive."}
