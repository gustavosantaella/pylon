from src.routes.app import api
from utils.response_json import response
from flask import jsonify


class UserController:
    
    @api.get("/")
    def hello_word():
        return response({"isWorking":True})