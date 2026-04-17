from app.db.database import Base

# Import all models here so SQLAlchemy metadata is aware of every table.
from app.models.booking import Booking
from app.models.car import Car
from app.models.user import User
