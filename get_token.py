import os
from dotenv import load_dotenv

load_dotenv()
def get_dkey(db):
    collection = db[os.environ.get('key_collection')]
    result = collection.find_one({"_id": os.environ.get('secret_key_id')})
    return result[os.environ.get('secret_key_field')]
