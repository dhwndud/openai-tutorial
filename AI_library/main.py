from typing import Union

from model.model import Item
from fastapi import FastAPI

app = FastAPI()

"""
CRUD
Create, Read, Update, Delete 

app.get
app.post
app.put
app.delete
"""


items = {
    0: {"name": "쏘마",
        "description": "somma"},
    1: {"name": "몬스터",
        "description": "Monster"},
    2: {"name": "오주영",
        "description": "OhJuyoung"},
}


# Path Parameter
@app.get("/{item_id}")
def read_root(item_id: int):
    item = items[item_id]
    return item


@app.get("/{item_id}/{key}")
def read_root(item_id: int, key: str):
    item = items[item_id][key]
    return item


# Query Parameter
@app.get("/item-by-name")
def read_item_bt_name(name: str):
    for item_id, item in items.items():
        if item['name'] == name:
            return item
        return {"error": "data not found"}


@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        return {"error": "there is already existing key"}
    items[item_id] = item.dict()
    return {"success": "ok"}

#
# @app.post("items/{item_id}")
# def update_item(item_id: int, item: Item):