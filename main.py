from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os, re

app = Flask(__name__)

CORS(app)
CORS(app, origins=[
    "http://localhost:5173/",
    "https://adam-fitrzyk.github.io/"
])

mongodb_connect_string = "mongodb://mongo:yjLewvdJzICKIDhpSqUdrZdxlFdMzKRC@[ballast.proxy.rlwy.net]:52013"
client = MongoClient(mongodb_connect_string)


# connect to db and return client
def connect_db(connection_string):
    client = MongoClient(connection_string)
    return client

def connect_coles(client):
    return client.get_database("coles")

def connect_woolies(client):
    return client.get_database("woolies")

# get every item from a database and return as a list of documents 
def get_items_from_collection(db, category):
    items = []
    cursor = db.get_collection(category).find({})
    for document in cursor:
        try:
            items.append(document)
        except:
            pass
    return items

# search the url of each item from database and compare with the search term
# to find all relevant items, return as a dictionary 
def find_items(search_term, items):
    relevant_items = []
    print(search_term)
    for item in items:
        print(item['name'])
        if re.search(f".*{search_term.lower()}.*", item['name'].lower()):
            relevant_items.append(item)
    return relevant_items
 

def package_result_as_json(coles_results, woolies_results):
    results = []
    for item in coles_results:
        result = {
            "name": item["name"],
            "store": item["store"],
            "price": item["price"],
            "unit": item["unit"],
            "weight": item["sub"],
            "stock": item["stock"],
            "url": item["url"]
        }
        results.append(result)
    for item in woolies_results:
        result = {
            "name": item["name"],
            "store": item["store"],
            "price": item["price"],
            "unit": item["unit"],
            "weight": item["weight"],
            "stock": item["stock"],
            "category": item["category"],
            "url": item["url"]
        }
        results.append(result)
    print(results)
    return jsonify(results)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

# grab search item from url
@app.route('/search/<item>')
def search(item):
    coles_db = connect_coles(client)
    woolies_db = connect_woolies(client)

    coles_items = get_items_from_collection(coles_db, 'fruits')
    woolies_items = get_items_from_collection(woolies_db, 'fruits')

    coles_relevant_items = find_items(item, coles_items)
    woolies_relevant_items = find_items(item, woolies_items)

    return package_result_as_json(coles_relevant_items, woolies_relevant_items)


# grab all items from mongodb
# grab every item with search item in name
# return all relevant items


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
