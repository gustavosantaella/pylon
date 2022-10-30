from .environment import env
from .database import databse_init

config = {
    "port": env('flask_port') or 3000,
    "database": {
        "provider": env("databasse_provider") or None,
        "port": None,
        "mongo_uri": env("mongo_uri")
    },
}
