from flask import Flask, request, make_response
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://HimaNovikaAgustina:Himanovika125@cluster0.3jxe7.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['HimaNovikaAgustina']
collection = db['sensor']

app = Flask(__name__)

sensor_data = {}

@app.route('/sensor', methods=['POST'])
def post_sensor():
    sensor_data = request.get_json()
    collection.insertOne(sensor_data)
    return make_response("Berhasil terkirim!")
    
@app.route('/sensor>', methods=['GET'])
def get_sensor():
    return sensor_data
    
if __name__ == '_main_':
    app.run(host="0.0.0.0", debug=True)