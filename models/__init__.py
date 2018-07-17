from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os


class Models:
    Base = declarative_base()
    engine = create_engine('sqlite:///D:\ExWIKI\main.db')
    Session = sessionmaker(bind=engine)

    @classmethod
    def drop(cls):
        cls.Base.metadata.drop_all(cls.engine)

    @classmethod
    def init(cls):
        cls.Base.metadata.create_all(cls.engine)














