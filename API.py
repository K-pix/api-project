from fastapi import FastAPI

app = FastAPI()

PRODUCTS = [
    {'name': 'Laptop', 'price': 1000, 'category': 'Electronics'},
    {'name': 'Chair', 'price': 100, 'category': 'Furniture'},
    {'name': 'Book', 'price': 20, 'category': 'Education'},
]

@app.get('/')
async def welcome():
    return {'message': 'Welcome to our product catalog'}

@app.get('/products')
async def get_all_products():
    return PRODUCTS

from fastapi import Body

@app.post('/products')
async def add_product(product: dict = Body()):
    PRODUCTS.append(product)
    return {'message': 'Product added successfully'}

@app.put('/products/{product_name}')
async def update_product(product_name: str, product: dict = Body()):
    for idx, existing_product in enumerate(PRODUCTS):
        if existing_product['name'] == product_name:
            PRODUCTS[idx] = product
            return {'message': 'Product updated successfully'}
