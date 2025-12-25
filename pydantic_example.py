from pydantic import BaseModel, Field


class Adress(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    #можно добавить свойства и функции
    is_active: bool = Field(alias="isActive")
    
    
user_data = {
    "id":11,
    "name": "Example",
    "email": "email",
    "isActive": True
}
user = User(**user_data)

print(user.model_dump())