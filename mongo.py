#THIS IS JUST A TEST FILE FROM ANOTHER TUTORIAL 
#IT USES A GET REQUEST TO GET DATA FROM THE DATABASE


from flask import Flask, jsonfiy, request
from flask.ext.pymongo import Pymongo
from pymongo import MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'environmental_db'
app.config['MONGO_URI'] = 'URI HERE'

mongo = PyMongo(app)

#THIS ROUTE WILL OUTPUT ALL COUNTRIES
@app.route('/countries', methods=['GET'])
def get_all_countries():
    countries = mongo.db.COLLECTIONINDATABASE

    output = []

    for q in countries.find():
        output.append({'name' : q['name'], 'other value' : q['other value']})

    return jsonify({'result' : output})

@app.route('/countries/<name>', method=['GET'])
def get_one_country(name):
    country = mongo.db.country

    q = country.find_one({'name' : name})
    output = {'name' : q['name'], 'other value' : q['other value']}

    return jsonify({'result' : output})