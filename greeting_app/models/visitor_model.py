from .db import db
from sqlalchemy import inspect

class Visitor(db.Model):
    __tablename__ = "visitors"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)

    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }


    @staticmethod
    def already_greeted(name):
        if Visitor.query.filter_by(name=name).first() == None:
            return False
        return True

    @staticmethod
    def add_greeted_name(name):
        new_visitor = Visitor(name=name)
        db.session.add(new_visitor)
        db.session.commit()

    @staticmethod
    def get_all_visitors():
        return Visitor.query.all()