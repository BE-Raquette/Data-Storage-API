from datetime import datetime

from bson import ObjectId
from fastapi import APIRouter, Response

from models import SessionModel
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
        return response
    else:
        return Response(status_code=400, content="Invalid session ID.")


@router.post("/start_new")
async def start_session(session: SessionModel):
    session = SESSION_MODEL.copy()
    session["start_time"] = datetime.now()
    session_id = database_interface.start_session(session)
    response = session_id
    return response


@router.put("/{session_id}/end")
async def end_session(session_id: str):
    session = database_interface.get_session(session_id)
    if session:
        session["end_time"] = datetime.now()
        database_interface.update_session(session)
        response = session
    else:
        response = Response(status_code=404, content="Session not found.")
    return response
