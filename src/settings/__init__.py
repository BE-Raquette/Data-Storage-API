from os import path
# DB
URI = "mongodb+srv://racketsensorsdata.ktzdeuf.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
CERT_FILE = path.join("..", "X509cert.pem")
DB_NAME = "RacketSensorsData"
SESSIONS_COLLECTION = "sessions"