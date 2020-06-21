from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient

#insert DATABASE CODE HERE
client = MongoClient("mongodb+srv://user01:user01@cluster0-ujqto.mongodb.net/apptest?retryWrites=true&w=majority")
db = client.get_database("apptest")
frameworks = db.frameworks

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'apptest'
app.config['MONGO_URI'] = 'mongodb+srv://user01:user01@cluster0-ujqto.mongodb.net/apptest?retryWrites=true&w=majority'
 #collection name
mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/example', methods=["GET"])
def framework(): 
    frame = []
    for q in frameworks.find():
        frame.append({'name' : q['name'], 'language' : q['language']})

    frame2 = []
    for q in frameworks.find():
        frame2.append(q['name'])

    return render_template('example.html', myframe=frame, myframe2=frame2)
    


#@app.route('/about', methods=['GET'])
# def get_all_frameworks():
#    return render_template('/about.html', name = "Celin")

# @app.route('/framework/<name>', methods=['GET'])
# def get_one_framework(name):
#     framework = mongo.db.frameworks 

#     q = framework.find_one({'name' : name})
#     output = {'name' : q['name'], 'language' : q['language']}

#     return jsonify({'result' : output})

# @app.route('/framework', methods=['POST'])
# def add_framework():
#     framework = mongo.db.frameworks 

#     name = request.json['name']
#     language = request.json['language']

#     framework_id = framework.insert({'name' : name, 'language' : language})
#     new_framework = framework.find_one({'_id' : framework_id})

#     output = {'name' : new_framework['name'], 'language' : new_framework['language']}

#     return jsonify({'result' : output})



    

if __name__ == '__main__':
    app.run(debug=True)