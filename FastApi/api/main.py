from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

fakedb=[]

class Product(BaseModel):
    id:int
    name:str
    description:str
    category:str
    brand:str
    gender:str
    size:float
    price: float
    imageUrl:str

@app.get("/")
def read_root():
    return {"greetings":"Welcome to Shopoholic"}

@app.get("/products")
def get_products():
    return fakedb

@app.get("/products/{product_id}")
def get_a_product(product_id:int):
    product=product_id -1
    return fakedb[product]

@app.post("/products")
def add_product(product:Product):
    fakedb.append(product.dict())
    return fakedb[-1]

@app.delete("/products/{product_id}")
def delete_product(product_id:int):
    fakedb.pop(product_id -1)
    return {"task":"deletion successful"}