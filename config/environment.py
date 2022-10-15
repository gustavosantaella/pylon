from dotenv import load_dotenv
import os
load_dotenv()

def env(key):
    key_env = key.upper()
    if key_env not in os.environ:
        return False
    return os.environ.get(key_env)