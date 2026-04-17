from sqlalchemy import Column,Integer,String,Float
from app.db.database import Base
class Car(Base):
    __tablename__="cars"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    brand=Column(String,nullable=False)
    price_per_day=Column(Float,nullable=False)
    available=Column(String,default="yes")