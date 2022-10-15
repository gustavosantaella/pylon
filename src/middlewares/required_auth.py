from flask import request, abort, jsonify
from utils.jwt import JWT
from jwt import ExpiredSignatureError, InvalidSignatureError

def required_auth(next, *arg, **args):
    try:
        if 'Authorization' not in request.headers:
            abort(401)
        token :str= request.headers["Authorization"].split(' ')[1]
        if token.strip() == '':
            abort(401)  
        token = JWT.decode(token)
        return next(user_id=token["user_id"], *arg, **args)
    except (ExpiredSignatureError, InvalidSignatureError) as e:
        message = str(e)
        if message in JWT.TOKEN_EXPIRED:
            return jsonify(JWT.TOKEN_EXPIRED)
        return jsonify(message)
        # abort(401)