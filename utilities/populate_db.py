from pymongo import MongoClient

connection_string = "mongodb://mongo:yjLewvdJzICKIDhpSqUdrZdxlFdMzKRC@[ballast.proxy.rlwy.net]:52013"

client = MongoClient(connection_string)

items = [
  {
    "name": "Coles Bananas",
    "store": "Coles",
    "price": 0.88,
    "unit": "$4.90/kg",
    "sub": "180g",
    "stock": "In Stock",
    "url": "https://www.coles.com.au/product/coles-bananas-approx.-180g-409499"
  },
  {
    "name": "Coles Strawberries",
    "store": "Coles",
    "price": 4.5,
    "unit": "$18.00/kg",
    "sub": "250g",
    "stock": "In Stock",
    "url": "https://www.coles.com.au/product/coles-strawberries-250g-5191256"
  },
  {
    "name": "Coles White Seedless Grapes",
    "store": "Coles",
    "price": 5.0,
    "unit": "$5.00/kg",
    "sub": "1kg",
    "stock": "In Stock",
    "url": "https://www.coles.com.au/product/coles-white-seedless-grapes-approx.-1kg-8133391"
  },
  {
    "name": "Coles Raspberries",
    "store": "Coles",
    "price": 4.0,
    "unit": "$32.00/kg",
    "sub": "125g",
    "stock": "In Stock",
    "url": "https://www.coles.com.au/product/coles-raspberries-125g-134029"
  },
  {
    "name": "Coles Hass Avocados",
    "store": "Coles",
    "price": 1.5,
    "unit": "$1.50/ea",
    "sub": "1 each",
    "stock": "In Stock",
    "url": "https://www.coles.com.au/product/coles-hass-avocados-1-each-5900530"
  },
  {
    "name": "Coles Blueberries",
    "store": "Coles",
    "price": 5.5,
    "unit": "$44.00/kg",
    "sub": "125g",
    "stock": "In Stock",
    "url": "https://www.coles.com.au/product/coles-blueberries-125g-5543535"
  },
  {
    "name": "Coles Seedless Watermelon Cut",
    "store": "Coles",
    "price": 5.22,
    "unit": "$2.90/kg",
    "sub": "1.8kg",
    "stock": "In Stock",
    "url": "https://www.coles.com.au/product/coles-seedless-watermelon-cut-approx.-1.8kg-7508229"
  },
  {
    "name": "Coles Pink Lady Apples",
    "store": "Coles",
    "price": 1.78,
    "unit": "$8.90/kg",
    "sub": "200g each",
    "stock": "In Stock",
    "url": "https://www.coles.com.au/product/coles-pink-lady-apples-medium-approx.-200g-each-5111654"
  },
  {
    "name": "Coles Royal Gala Apples",
    "store": "Coles",
    "price": 1.34,
    "unit": "$7.90/kg",
    "sub": "170g",
    "stock": "In Stock",
    "url": "https://www.coles.com.au/product/coles-royal-gala-apples-loose-approx.-170g-5226000"
  },
  {
    "name": "Coles Granny Smith Apples",
    "store": "Coles",
    "price": 1.34,
    "unit": "$7.90/kg",
    "sub": "170g",
    "stock": "In Stock",
    "url": "https://www.coles.com.au/product/coles-apple-granny-smith-medium-approx.-170g-408554"
  }
]

if __name__ == "__main__":
    try:
        coles = client.get_database("coles")
        vegs = coles.get_collection("fruits")
        for item in items:
            vegs.insert_one(item)
    except Exception as e:
        print("Could not insert to database because of error: ", e)
