from collections import OrderedDict
from datetime import datetime
from json import dumps, loads
from pprint import pprint

from profiler import db, app  # type: ignore

# CONSTANTS


def documentation():
    """ DOCUMENTATION """


# noinspection PyUnresolvedReferences
class HouseKeeping(object):

    def save(self, commit=True):
        if commit:
            instance = self
            if not instance.id:
                db.session.add(instance)

            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return False

            return True
        return False


    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.id)

    @classmethod
    def columns(cls):
        return cls.__table__.columns.keys()




class Base(db.Model, HouseKeeping):  # type: ignore
    """Base model that other models inherit from"""

    __abstract__ = True

    id = db.Column(db.String, primary_key=True, nullable=False)  # type: ignore
    active = db.Column(db.Boolean, nullable=False, default=True)  # type: ignore
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # type: ignore
    updated_at = db.Column(  # type: ignore
        db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow  # type: ignore
    )


def cleanup():
    db.session.rollback()
    db.session.commit()
    print("DB in a clean state")


def latest(_class):
    db.engine.echo = False
    try:
        print("\n")
        return _class.query.order_by(_class.id.desc()).first().display()
    except (Exception,):
        cleanup()
        print("\nNo data found")


# noinspection PyProtectedMember
def show_all():
    classes, models, table_names = [], [], []
    for clazz in db.Model._decl_class_registry.values():
        if hasattr(clazz, "__tablename__"):
            table_names.append(clazz.__tablename__)
            classes.append(clazz)

    for table in db.metadata.tables.items():
        if table[0] in table_names:
            models.append(classes[table_names.index(table[0])])

    return classes, models, table_names

def date_handler(value):
    """
    Return a string type of Python datetime format
    :param value: datetime of Python
    :return: string
    """
    return value.isoformat() if hasattr(value, "isoformat") else value
