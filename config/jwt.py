from config.environment import env

algorithm= env("jwt_algorithm") or "HS256"