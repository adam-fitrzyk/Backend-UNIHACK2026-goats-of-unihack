from pymongo import MongoClient
import pprint

mongodb_connect_string = "mongodb://mongo:yjLewvdJzICKIDhpSqUdrZdxlFdMzKRC@[ballast.proxy.rlwy.net]:52013"

client = MongoClient(mongodb_connect_string)

if (__name__ == "__main__"):
    try:
        database = client.get_database("coles")
        coles = database.get_collection("vegetables")

        cursor = coles.find({})
        for document in cursor:
            pprint.pprint(document)

    except Exception as e:
        raise Exception("Unable to find document due to following error: ", e)
