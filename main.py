# app/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, query_param: str = None):
    return {
        "item_id": item_id, 
        "query_param": query_param
        }
