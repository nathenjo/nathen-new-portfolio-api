from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
import certifi
from markupsafe import escape
from auth_middleware import token_required
from get_token import get_dkey

app = Flask(__name__)

client = MongoClient(os.environ.get('connection_string'), tlsCAFile=certifi.where())
db = client['Nate-New-Portfolio']
collection = db['dynamic-data']

app.config['SECRET_KEY'] = get_dkey(db)

@app.route('/')
def hello_world():
    return "<h1>API For Nathen Johnson Portfolio</h1>"

@app.route('/<param>', methods=['GET'])
def social_links(param):
    if token_required(request) == True:
        if request.method == 'GET':
            search = request.args.get('search')
            result = collection.find_one({param: search})
            return jsonify(result)
        else:
            return 'HTTP Method must be GET'
    else:
        return token_required(request)
