from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CommonColumns(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))


class Styles(CommonColumns):
    __tablename__ = 'styles'


class Yeast(CommonColumns):
    __tablename__ = 'yeast'


class Hops(CommonColumns):
    __tablename__ = 'hops'


class Fermentables(CommonColumns):
    __tablename__ = 'fermentables'
