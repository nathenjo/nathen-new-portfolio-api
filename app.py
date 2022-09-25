from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient as MC

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>API For Nathen Johnson Portfolio</h1>"