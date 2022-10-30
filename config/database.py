from mongoengine import connect


def databse_init(config):
    provider = config["provider"] 
    if not provider:
        return None
    match provider:
        case "mysql":
            pass
        case "postgres":
            pass
        case "mongodb":
            return connect(host=config['mongo_uri'])
        case _:
            return  None
