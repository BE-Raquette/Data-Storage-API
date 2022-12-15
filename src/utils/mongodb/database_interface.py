from pymongo import MongoClient

from settings import URI, DB_NAME, SESSIONS_COLLECTION, CERT_FILE


class DatabaseInterface:
    def __init__(self):
        self.client = MongoClient(URI,
                                  tls=True,
                                  tlsCertificateKeyFile=CERT_FILE)
        self.db = self.client[DB_NAME]
        self.sessions = self.db[SESSIONS_COLLECTION]

database_interface = DatabaseInterface()
