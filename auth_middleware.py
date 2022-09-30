from functools import wraps
from flask import current_app
from pymongo import MongoClient
import os
import certifi

client = MongoClient(os.environ.get('connection_string'), tlsCAFile=certifi.where())
db = client['Nate-New-Portfolio']
collection = db[os.environ.get('key_collection')]

def token_required(request):
    token = None
    if "api-key" in request.headers:
        token = request.headers["api-key"]
    if not token:
        return {
            "message": "Authentication Token is missing!",
            "data": None,
            "error": "Unauthorized"
        }, 401
    try:
        auth_token=collection.find_one({"_id": token})
        if auth_token[os.environ.get('query_key')] == current_app.config['SECRET_KEY']:
            return True
        elif auth_token is None:
            return {
            "message": "Invalid Authentication token!",
            "data": None,
            "error": "Unauthorized"
        }, 401
        else:
            return False
    except Exception as e:
        return {
            "message": "Something went wrong",
            "data": None,
            "error": str(e)
        }, 500