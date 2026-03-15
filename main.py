from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bs4 import BeautifulSoup
import os, re, requests

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

# get every item from a database and return as a list of urls 
def get_items_from_collection(db, category):
    items = []
    cursor = db.get_collection(category).find({})
    for document in cursor:
        try:
            items.append(document['url'])
        except:
            pass
    return items

# search the url of each item from database and compare with the search term
# to find all relevant items, return as a dictionary 
def find_items(item, urls):
    relevant_items = []
    for url in urls:
        if re.search(f".*{item.lower()}.*", url):
            relevant_items.append(url)
            print(item.lower(), url)
    return relevant_items
 

def package_result_as_json(coles_results, woolies_results):
    results = []
    for item in coles_results:
        results.append({'brand': 'coles', 'url': item})
    for item in woolies_results:
        results.append({'brand': 'woolies', 'url': item})
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

    coles_items = get_items_from_collection(coles_db, 'vegetables')
    woolies_items = get_items_from_collection(woolies_db, 'vegetables')

    coles_relevant_items = find_items(item, coles_items)
    woolies_relevant_items = find_items(item, woolies_items)

    return package_result_as_json(coles_relevant_items, woolies_relevant_items)


# grab all items from mongodb
# grab every item with search item in name
# return all relevant items


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
