from src.routes import api
from utils.response_json import response

@api.get("/auth/login")
def login():
    return response("23")