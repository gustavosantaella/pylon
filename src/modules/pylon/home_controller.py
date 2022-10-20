from src.routes.app import api
from utils.response_json import response
from flask import jsonify

@api.get("/")
def hello_word():
    return response({"isWorking":True})