from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient

#insert DATABASE CODE HERE
client = MongoClient("mongodb+srv://environmental:environmental@cluster0-jq5lb.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.get_database("environmental_db")
countries = db.theme_result_count

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'environmental_db'
app.config['MONGO_URI'] = 'mongodb+srv://environmental:environmental@cluster0-jq5lb.mongodb.net/<dbname>?retryWrites=true&w=majority'
 #collection name
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/countries', methods=["GET"])
def country(): 
    frame1 = []
    for q in countries.find(): 
        frame1.append({q['ID'], q['value']})
    
    frame2 = []
    for q in countries.find():
        frame2.append(q['value'])
    print(q)
    return render_template('countries.html', myframe1=frame1, myframe2=frame2)
    
@app.template_filter('england')
def england_filter(england):
    englandFiltered = [x for x in xyz  if 'ID' in x and x['ID'].endswith('_england')]
    return englandFiltered


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