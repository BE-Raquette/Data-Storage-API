from bson import ObjectId

from pymongo import MongoClient

from settings import URI, DB_NAME, SESSIONS_COLLECTION, CERT_FILE


class DatabaseInterface:
    def __init__(self) -> None:
        self.client = MongoClient(URI,
                                  tls=True,
                                  tlsCertificateKeyFile=CERT_FILE)
        self.db = self.client[DB_NAME]
        self.sessions = self.db[SESSIONS_COLLECTION]

    def get_all_sessions(self) -> list[dict]:
        cursor = self.sessions.find({})
        sessions = list(cursor)
        self.stringify_object_ids(sessions)
        return sessions

    def get_session(self, session_id: str) -> dict or None:
        session = self.sessions.find_one({"_id": ObjectId(session_id)})
        self.stringify_object_ids(session)
        return session

    def start_session(self, session: dict) -> str:
        inserted_id = self.sessions.insert_one(session).inserted_id
        return str(inserted_id)

    def update_session(self, session: dict) -> None:
        _id = session.pop("_id")
        self.sessions.update_one({"_id": ObjectId(_id)}, {"$set": session})

    @staticmethod
    def stringify_object_ids(data: dict or list) -> None:
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, ObjectId):
                    data[key] = str(value)
                elif isinstance(value, dict):
                    DatabaseInterface.stringify_object_ids(value)
                elif isinstance(value, list):
                    for item in value:
                        if isinstance(item, dict):
                            DatabaseInterface.stringify_object_ids(item)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, ObjectId):
                    data[data.index(item)] = str(item)
                elif isinstance(item, dict):
                    DatabaseInterface.stringify_object_ids(item)
                elif isinstance(item, list):
                    DatabaseInterface.stringify_object_ids(item)

    def clear_database(self) -> None:
        delete_count = self.sessions.delete_many({}).deleted_count
        print(f"Deleted {delete_count} sessions.")


database_interface = DatabaseInterface()
