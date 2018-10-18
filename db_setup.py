import sys

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# ^^^^^    Boilerplate    ^^^^^ #


# _____ Unique to project _____ #

class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)

    name = Column(String(80), nullable=False)


class Menu(Base):
    __tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)

    name = Column(String(80), nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))

    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))

    restaurant = relationship(Restaurant)


# _____ Need this at bottom _____ #

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
