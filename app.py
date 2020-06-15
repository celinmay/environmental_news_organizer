from flask import Flask, render_template
from data import Countries
from pymongo import MongoClient
#from flask_pymongo import PyMongo

#mongo = PyMongo()

#insert DATABASE CODE HERE
#client = MongoClient("?????")
#db = client.get_database('environmental_db')
#put username here
#records = db.????

app = Flask(__name__)
#mongo.init_app(app)

Countries = Countries()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/countries')
def countries():
    return render_template('countries.html', countries = Countries)

@app.route('/country/<string:id>/')
def article(id):
    return render_template('country.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)