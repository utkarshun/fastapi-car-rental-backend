from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from app.routes import car_routes, user_routes,booking_routes
app=FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(car_routes.router)
app.include_router(user_routes.router)
app.include_router(booking_routes.router)
@app.get("/")
def home():
    return {"message":"Car Rental API Running"}