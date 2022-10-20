from flask import jsonify
def Error(error):
    if type(error) is ApiError:    
        return jsonify({
            "code": error.code,
            "errors":[],
            "message": error.message,
            "data":{}
        })
    else:
        return jsonify({
            "code": 400,
            "errors":[],
            "message": str(error),
            "data":{}
        })


class ApiError(Exception):
    code = 400,
    message = "Bad Request"
    
    def __init__(self, code, message):
        self.code = code
        self.message = message