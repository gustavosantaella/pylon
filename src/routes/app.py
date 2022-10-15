from flask import Blueprint

web = Blueprint("web_routes", __name__)
api = Blueprint("api_routes", __name__, url_prefix="/api")
