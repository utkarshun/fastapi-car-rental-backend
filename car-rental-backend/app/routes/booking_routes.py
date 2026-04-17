from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.booking import Booking
from app.models.car import Car
from app.models.user import User
from app.schemas.booking import BookingCreate,BookingResponse
router=APIRouter()
@router.post("/book",response_model=BookingResponse)
def book_car(booking:BookingCreate,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==booking.user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")

    car=db.query(Car).filter(Car.id==booking.car_id).first()
    if not car:
        raise HTTPException(status_code=404,detail="Car not found")
    if car.available!="yes":
        raise HTTPException(status_code=400,detail="Car not available")
    
    new_booking=Booking(
        user_id=booking.user_id,
        car_id=booking.car_id,
        start_date=booking.start_date,
        end_date=booking.end_date
    )
    car.available="no"
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking