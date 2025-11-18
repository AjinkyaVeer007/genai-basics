from pydantic import BaseModel

class User(BaseModel):
    id:int
    name: str
    is_active: bool

user_data = {
    "id": 101,
    "name" : "Ajinkya",
    "is_active": True
}

user = User(**user_data)
print(user)