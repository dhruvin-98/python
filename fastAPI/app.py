from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get('/')
def hello():
    return "hello....1"

products = [
    Product(id=1,name="Phone",description="A mobile",price=699,quantity=50),
    Product(id=2,name="watch",description="A Titan",price=80,quantity=88),
    Product(id=3,name="charger",description="A charger",price=40,quantity=100),
    
]

@app.get('/product')
def get_product():
    return products

@app.get("/product/{id}")
def get_bproduct_byid(id : int):
    for product in products:
        if product.id == id:
            return product

    return "Product not found"

@app.post("/product")
def add_product(product : Product):
    products.append(product)
    return product