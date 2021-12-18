import datetime
from profiler import db
from profiler.models import Base
from sqlalchemy.dialects.postgresql import ENUM

class Profile(Base):
    __tablename__ = 'profile'

    title = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    middle_name = db.Column(db.String(120), nullable=True)
    gender = db.Column("gender", ENUM("male", "female", "other", name="gender_enum"), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    nationality = db.Column(db.Text, nullable=False)

    def get_all(self, limit=100):
        pass

