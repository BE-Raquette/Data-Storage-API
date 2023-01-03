from fastapi import Query
from pydantic import BaseModel


class PlayerDataModel(BaseModel):
    """Player Data Model"""
    height: int = Query(..., description="Player height in cm", example=180, gt=0)
    weight: int = Query(..., description="Player weight in kg", example=80, gt=0)
    age: int = Query(..., gt=0, lt=150, description="Player age in years", example=25)
    gender: str = Query(None, regex="F|M|O", description="Gender of the player", example="M")


class SessionModel(BaseModel):
    """Session Model"""
    player_data: PlayerDataModel
    sensors: list
    data: list
