#  Using a use-case of your choice, apply the concepts of ORM and SQLAlchemy to demonstrate these functionalities ~ Create, Read, Update, and Delete with SQLAlchemy. Due: 12pm

#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    population = Column(Integer())
    governor = Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///cities.db')
    Base.metadata.create_all(engine)

     # use our engine to configure a 'Session' class
    Session = sessionmaker(bind=engine)
    # use 'Session' class to create 'session' object
    session = Session()

    city1 = City(
        name ="Nairobi City",
        population = "57463636",
        governor = "Hon. Sakaja"
    )
    city2 = City(
        name ="Mombasa City",
        population = "47465636",
        governor = "Hon. Abdi"
    )
    city3 = City(
        name ="Kisumu City",
        population = "64789389",
        governor = "Hon. Anyang' Ny'ong'o"
    )
    city4 = City(
        name ="Nakuru City",
        population = "36770830",
        governor = "Hon. Lee Kinyanjui"
    )
    
# INSERT INTO cities
    session.add_all([city1,city2,city3,city4])
    session.commit()

    session.bulk_save_objects([city1, city1, city2, city3, city4])
    session.commit()

# READ
    cities = session.query(City).all()
    for city in cities:
       print(city.governor)

# Update
    query = session.query(City).filter(City.name == "Nairobi City").first()
    query.name = "Nakuru City"
    session.commit()
    
# delete cities
    # query = session.query(City).filter(City.name == "Nakuru City").first()
    # # session.delete(query)
    # # session.commit()
    # print(query)
    
    