import os
import json

from fastapi import FastAPI

from models import StoreItem, CreateStoreItemRequest

app = FastAPI()


def load_items() -> list[StoreItem]:
    with open("store_items.json", "r") as file:
        data = json.load(file)
    return [StoreItem(**item) for item in data]


def write_item(items: list[StoreItem]):
    items_dict = [obj.model_dump() for obj in items]
    with open("store_items.json", "w") as file:
        json.dump(items_dict, file, indent=4)


@app.get("/")
async def get_items() -> list[StoreItem]:
    items = load_items()
    return items


@app.post("/")
async def create_item(item: CreateStoreItemRequest) -> str:
    items = load_items()
    new_id = items[-1].id + 1
    new_item = StoreItem(
        id=new_id, name=item.name, description=item.description, price=item.price
    )
    items.append(new_item)
    write_item(items)
    return "Item added successfully"


@app.put("/")
async def update_item(item: CreateStoreItemRequest, id: int = 0) -> str:
    items = load_items()
    items[id - 1] = StoreItem(
        id=id, name=item.name, description=item.description, price=item.price
    )
    write_item(items)
    return f"Item {id} updated successfully"


@app.delete("/")
async def delete_item(id: int = 0) -> str:
    items = load_items()
    items.pop(id - 1)
    for i in range(len(items)):
        items[i].id = i + 1
    write_item(items)
    return f"Item {id} deleted successfully"
