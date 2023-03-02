from datetime import datetime

from bson import ObjectId
from fastapi import APIRouter, Response

from models import SessionModel, PlayerDataModel
from utils.mongodb import database_interface
from settings import SESSION_MODEL

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.get("/get_all")
async def get_all_sessions():
    response = database_interface.get_all_sessions()
    return response


@router.get("/{session_id}/data")
async def get_session(session_id: str):
    if ObjectId.is_valid(session_id):
        session = database_interface.get_session(session_id)
        if session:
            response = session
        else:
            response = Response(status_code=404, content="Session not found.")
    else:
        response = Response(status_code=400, content="Invalid session ID.")
    return response


@router.post("/start")
async def start_session(player_data: PlayerDataModel):
    session = SESSION_MODEL.copy()
    session["start_time"] = datetime.now()
    session["player_data"] = player_data.dict()
    session_id = database_interface.start_session(session)
    return {
        "session_id": session_id
    }
