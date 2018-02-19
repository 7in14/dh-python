from pymongo import MongoClient
import pprint
from app import app


@app.route('/')
@app.route('/ping')
def ping():
    return "pong"


@app.route('/dataSources')
def data_sources():
    client = MongoClient()
    db = client.admin
    serverStatus = db.command("serverStatus")
    return pprint.pformat(serverStatus, indent=2)
