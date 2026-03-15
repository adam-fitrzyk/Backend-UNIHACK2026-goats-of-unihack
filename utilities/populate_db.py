from pymongo import MongoClient

connection_string = "mongodb://mongo:yjLewvdJzICKIDhpSqUdrZdxlFdMzKRC@[ballast.proxy.rlwy.net]:52013"

client = MongoClient(connection_string)

items = [
    {
        "name": "Woolworths Cavendish Bananas",
        "store": "Woolworths",
        "price": 0.81,
        "unit": "$0.81/ea",
        "weight": None,
        "stock": "In Stock",
        "category": "Fruit",
        "url": "https://www.woolworths.com.au/shop/productdetails/133211/cavendish-bananas"
    },
    {
        "name": "Woolworths Fresh Pink Lady Apples",
        "store": "Woolworths",
        "price": 1.56,
        "unit": "$1.56/ea",
        "weight": None,
        "stock": "In Stock",
        "category": "Fruit",
        "url": "https://www.woolworths.com.au/shop/productdetails/105919/fresh-pink-lady-apples"
    },
    {
        "name": "Woolworths Strawberries Punnet",
        "store": "Woolworths",
        "price": 4.50,
        "unit": "$18.00/kg",
        "weight": "250g",
        "stock": "In Stock",
        "category": "Fruit",
        "url": "https://www.woolworths.com.au/shop/productdetails/144607/strawberries-punnet"
    },
    {
        "name": "Woolworths White Seedless Grapes Bag",
        "store": "Woolworths",
        "price": 5.50,
        "unit": "$5.50/ea",
        "weight": "900g",
        "stock": "In Stock",
        "category": "Fruit",
        "url": "https://www.woolworths.com.au/shop/productdetails/138801/white-seedless-grapes-bag-approx-900g"
    },
    {
        "name": "Woolworths Avocado Shepard",
        "store": "Woolworths",
        "price": 1.30,
        "unit": "$1.30/ea",
        "weight": None,
        "stock": "In Stock",
        "category": "Fruit",
        "url": "https://www.woolworths.com.au/shop/productdetails/186910/avocado-shepard"
    },
    {
        "name": "Woolworths Blueberries Punnet",
        "price": 6.00,
        "unit": "$48.00/kg",
        "weight": "125g",
        "stock": "In Stock",
        "category": "Fruit",
        "url": "https://www.woolworths.com.au/shop/productdetails/169792/blueberries-punnet"
    },
    {
        "name": "Woolworths Apple Royal Gala",
        "store": "Woolworths",
        "price": 1.26,
        "unit": "$1.26/ea",
        "weight": None,
        "stock": "In Stock",
        "category": "Fruit",
        "url": "https://www.woolworths.com.au/shop/productdetails/155003/apple-royal-gala"
    },
    {
        "name": "Woolworths Fresh Granny Smith Apples",
        "store": "Woolworths",
        "price": 1.38,
        "unit": "$1.38/ea",
        "weight": None,
        "stock": "In Stock",
        "category": "Fruit",
        "url": "https://www.woolworths.com.au/shop/productdetails/130935/fresh-granny-smith-apples"
    },
    {
        "name": "Woolworths Red Watermelon Cut Quarter",
        "store": "Woolworths",
        "price": 6.38,
        "unit": "$6.38/ea",
        "weight": None,
        "stock": "In Stock",
        "category": "Fruit",
        "url": "https://www.woolworths.com.au/shop/productdetails/120384/woolworths-red-watermelon-cut-quarter"
    },
    {
        "name": "Woolworths Raspberries Punnet",
        "store": "Woolworths",
        "price": 5.90,
        "unit": "$34.71/kg",
        "weight": "170g",
        "stock": "In Stock",
        "category": "Fruit",
        "url": "https://www.woolworths.com.au/shop/productdetails/453364/raspberries-punnet"
    }
]

if __name__ == "__main__":
    try:
        coles = client.get_database("woolies")
        vegs = coles.get_collection("fruits")
        for item in items:
            vegs.insert_one(item)
    except Exception as e:
        print("Could not insert to database because of error: ", e)
