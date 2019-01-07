from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo


app = Flask(__name__)
Bootstrap(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flasktrap"
mongo = PyMongo(app)


##Insert products in the database
#product = {"code": 1, "name": "prod1", "username": "user1", "description": "prod1 test"}
#mongo.db.products.insert_one(product)
#product = {"code": 2, "name": "prod2", "username": "user2", "description": "prod2 test"}
#mongo.db.products.insert_one(product)
#product = {"code": 3, "name": "prod3", "username": "user3", "description": "prod3 test"}
#mongo.db.products.insert_one(product)

#product = {"code": 4, "name": "prod4", "username": "user4", "description": "prod4 test"}
#mongo.db.products.insert_one(product)
#product = {"code": 5, "name": "prod5", "username": "user5", "description": "prod5 test"}
#mongo.db.products.insert_one(product)
#product = {"code": 6, "name": "prod6", "username": "user6", "description": "prod6 test"}
#mongo.db.products.insert_one(product)


@app.route("/", methods=('GET', 'POST'))
def index():
    products = list(mongo.db.products.find())
    return render_template('index.html', products=products)


@app.route("/search")
def search():
    query = request.args.get('query', '')
    code = int(request.args.get('code_prod', '-1'))
    products = list(mongo.db.products.find({'$or':[{"name": query}, {"code": code}] }))
    return render_template('index.html', products=products)


@app.route("/product/<int:id>")
def product(id):
    return render_template('product.html')
