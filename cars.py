from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///cars.db')


class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    make = Column(String)
    model = Column(String)
    capacity = Column(Float)
    model_type = Column(String)
    first_registration = Column(Integer)
    fuel = Column(String)
    gearbox = Column(String)
    power = Column(Integer)
    mileage = Column(Integer)
    city = Column(String)

    def __init__(self, price, make, model, capacity, model_type, first_registration,
                 fuel, gearbox, power, mileage, city):
        self.price = price
        self.make = make
        self.model = model
        self.capacity = capacity
        self.model_type = model_type
        self.first_registration = first_registration
        self.fuel = fuel
        self.gearbox = gearbox
        self.power = power
        self.mileage = mileage
        self.city = city


Base.metadata.create_all(engine)
