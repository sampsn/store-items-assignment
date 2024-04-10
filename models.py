from pydantic import BaseModel


class StoreItem(BaseModel):
    id: int
    name: str
    description: str
    price: float


class CreateStoreItemRequest(BaseModel):
    name: str
    description: str
    price: float
