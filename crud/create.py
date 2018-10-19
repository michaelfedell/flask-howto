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

# creating an entry in db is easy as creating a new python object
firstRestaurant = Restaurant(name='Pizza Palace')

# the new object must be added to the current session
session.add(firstRestaurant)

# to save the changes in session we must commit
session.commit()

cheesepizza = MenuItem(
    name='Cheese Pizza',
    description='Made with all natural ingredients and fresh mozzarella',
    course='Entree',
    price='$8.99',
    restaurant=firstRestaurant)

session.add(cheesepizza)
session.commit()
