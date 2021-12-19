import datetime

from requests.sessions import session

from profiler import db
from profiler.models import Base
from profiler.models.profile_schema import profiles_schema
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

    def get_all(self, limit=50, page=1, per_page=None):
        
        if per_page is not None:

            profiles = db.session.query(Profile).paginate(page=page, per_page=per_page)
            data = profiles_schema.dump(profiles.items)

            meta = {
                "page": profiles.page,
                'pages': profiles.pages,
                'total_count': profiles.total,
                'prev_page': profiles.prev_num,
                'next_page': profiles.next_num,
                'has_next': profiles.has_next,
                'has_prev': profiles.has_prev,

            }

            return {'data': data, "meta": meta}
        else:

            profiles = db.session.query(Profile).limit(limit).all()
            data = profiles_schema.dump(profiles)

            return data
            

    def filter_by_columns(self, gender=None, title=None, nationality=None):
        pass

    def format(self):
        results = {
            'id': self.id,
            'title': self.title,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name': self.middle_name,
            'gender': self.gender,
            'dob': self.dob,
            'phone': self.phone,
            'email': self.email,
            'nationality': self.nationality
        }

        return results

