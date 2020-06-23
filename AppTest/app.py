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

england = [ ]

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
    
@app.route('/germany', methods=["GET"])
def germany(): 
        
    germany01 = []
    for q in countries.find():
        germany01.append(q['value'])
    print(q)
    return render_template('germany.html', len = len(germany01), listgermany=germany01)

@app.route('/england', methods=["GET"])
def england(): 
        
    england01 = []
    for q in countries.find():
        england01.append(q['value'])
    print(q)
    return render_template('england.html', listengland=england01)

@app.route('/denmark', methods=["GET"])
def denmark(): 
        
    denmark01 = []
    for q in countries.find():
        denmark01.append(q['value'])
    print(q)
    return render_template('denmark.html', listdenmark=denmark01)

@app.route('/france', methods=["GET"])
def france(): 
        
    france01 = []
    for q in countries.find():
        france01.append(q['value'])
    print(q)
    return render_template('france.html', listfrance=france01)

@app.route('/spain', methods=["GET"])
def spain(): 
        
    spain01 = []
    for q in countries.find():
        spain01.append(q['value'])
    print(q)
    return render_template('spain.html', listspain=spain01)

@app.route('/poland', methods=["GET"])
def poland(): 
        
    poland01 = []
    for q in countries.find():
        poland01.append(q['value'])
    print(q)
    return render_template('poland.html', listpoland=poland01)

@app.route('/italy', methods=["GET"])
def italy(): 
        
    italy01 = []
    for q in countries.find():
        italy01.append(q['value'])
    print(q)
    return render_template('italy.html', listitaly=italy01)

@app.route('/russia', methods=["GET"])
def russia(): 
        
    russia01 = []
    for q in countries.find():
        russia01.append(q['value'])
    print(q)
    return render_template('russia.html', listrussia=russia01)

@app.route('/greece', methods=["GET"])
def greece(): 
        
    greece01 = []
    for q in countries.find():
        greece01.append(q['value'])
    print(q)
    return render_template('greece.html', listgreece=greece01)
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