from pydantic import BaseModel
class CarCreate(BaseModel):
    name:str
    brand:str
    price_per_day:float

class CarResponse(BaseModel):
    id:int
    name:str
    brand:str
    price_per_day:float
    available:str
    class Config:
        from_attributes = True
        