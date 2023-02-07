from .sessions import router as sessions_router
from .data_collectors import router as data_router

routers = [sessions_router, data_router]
