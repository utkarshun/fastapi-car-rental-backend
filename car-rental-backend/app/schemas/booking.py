from pydantic import BaseModel
from datetime import date
class BookingCreate(BaseModel):
    user_id:int
    car_id:int
    start_date:date
    end_date:date
class BookingResponse(BaseModel):
    id:int
    user_id:int
    car_id:int
    start_date:date
    end_date:date

    class Config:
        orm_mode=True