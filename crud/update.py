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

veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')

for burger in veggieBurgers:
    print(burger.id, burger.price, burger.restaurant.name)

urbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
print(urbanVeggieBurger.id, urbanVeggieBurger.name, urbanVeggieBurger.price)

urbanVeggieBurger.price = '$2.99'
session.add(urbanVeggieBurger)
session.commit()

print('new price:', session.query(MenuItem).filter_by(id=8).one().price)

print('Update all veggie burgers!')

for burger in veggieBurgers:
    if burger.price != '$2.99':
        burger.price = '$2.99'
        session.add(burger)
session.commit()

for burger in veggieBurgers:
    print(burger.id, burger.price, burger.restaurant.name)
