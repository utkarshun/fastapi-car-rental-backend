from sqlalchemy import Column,Integer,ForeignKey,Date
from app.db.database import Base
class Booking(Base):
    __tablename__="bookings"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    car_id=Column(Integer,ForeignKey("cars.id"))
    start_date=Column(Date)
    end_date=Column(Date)
    