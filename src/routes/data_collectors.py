from bson import ObjectId
from fastapi import APIRouter, Response, Query

from utils.mongodb import database_interface

router = APIRouter(prefix="/data", tags=["data"])


@router.post("/{session_id}/{type}")
async def start_session(session_id: str, data: dict, type: str = Query(..., regex="smashs|forehand_strokes|backhand_strokes|volleys|serves")):
    if ObjectId.is_valid(session_id):
        if database_interface.add_data(session_id, type, data) == 0:
            response = Response(status_code=404, content="Session not found.")
        else:
            response = Response(status_code=200, content="OK")
    else:
        response = Response(status_code=400, content="Invalid session ID.")
    return response
