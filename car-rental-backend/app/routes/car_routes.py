from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.car import Car
from app.schemas.car import CarCreate, CarResponse
router = APIRouter()

@router.post("/cars",response_model=CarResponse)
def add_car(car:CarCreate,db:Session=Depends(get_db)):
    new_car=Car(
        name=car.name,
        brand=car.brand,
        price_per_day=car.price_per_day
    )
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car

@router.get("/cars",response_model=list[CarResponse])
def get_cars(db:Session=Depends(get_db)):
    return db.query(Car).all()

@router.put("/car/{car_id}",response_model=CarResponse)
def update_car(car_id:int,car:CarCreate,db:Session=Depends(get_db)):
    existing_car=db.query(Car).filter(Car.id==car_id).first()
    if not existing_car:
        raise HTTPException(status_code=404,detail="Car not found")
    existing_car.name=car.name
    existing_car.brand=car.brand
    existing_car.price_per_day=car.price_per_day
    
    db.commit()
    db.refresh(existing_car)
    return existing_car

@router.delete("/cars/{car_id}")
def delete_car(car_id:int,db:Session=Depends(get_db)):
    car=db.query(Car).filter(Car.id==car_id).first()
    
    if not car:
        raise HTTPException(status_code=404,detail="Car not found")
    db.delete(car)
    db.commit()
    
    return {"message":"Car deleted successfully"}