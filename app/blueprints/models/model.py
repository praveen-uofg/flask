from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy

from dataclasses import dataclass

db = SQLAlchemy()


@dataclass
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    age = db.Column(db.String(3), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    modified_date = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return u"<User(id=%r, first_name=%r,  last_name=%r," \
               u" age=%r)>" \
               % (self.id, self.first_name, self.last_name,
                  self.age)

    @property
    def user_id(self):
        return self.id

    @staticmethod
    def create_user(first_name, last_name, age):
        # create the user on Database
        u = User(first_name=first_name.strip(),
                 last_name=last_name.strip(),
                 age=age,)

        User.save_to_db(u)
        return u

    # Method to save user to DB
    def save_to_db(self):
        self.modified_date = dt.now()
        db.session.add(self)
        db.session.commit()

    # Method to remove user from DB
    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return dict(id=self.id,
                    first_name=self.first_name,
                    last_name=self.last_name,
                    age=self.age)
