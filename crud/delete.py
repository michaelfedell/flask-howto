from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Restaurant, MenuItem

# specify the database with which to connect
engine = create_engine('sqlite:///restaurantmenu.db')

# bind engine to base class
# this makes connections bt class definitions and corresponding tables
Base.metadata.bind = engine

# establish connection between code executions and created engine
# allows preparation of many commands before `committing` to database
DBSession = sessionmaker(bind=engine)

# create a singular session to execute some code
# this session will act as a staging ground - none of the changes
# made within the session will persist unless session.commit is called
session = DBSession()

spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
print(spinach.restaurant.name)

session.delete(spinach)
# session.commit()

# spinach = session.query(MenuItem).filter_by(name='Spinach Ice Cream').one()
