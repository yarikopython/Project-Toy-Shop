from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
import sqlalchemy
import sqlalchemy.orm
import csv

url = "sqlite:///./db.sqlite3"
engine = create_engine(url)


session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.orm.declarative_base()

class Toy(Base):
    __tablename__ = "toys"
    id = Column(Integer, primary_key=True)
    name =  Column(String)
    price = Column(Float(precision=2), default=0.0)
    category = Column(String)
    amount = Column(Integer, default=0)

Base.metadata.create_all(bind=engine)

toys = session_local().query(Toy).all()

            
def create_toy(name: str, price: float, category: str, amount: int):
    with session_local() as session:
        new_toy = Toy(name=name, price=price, category=category, amount=amount)
        toys_name = [toy.name for toy in toys]
        if new_toy.name not in toys_name:
            session.add(new_toy)
            session.commit()
            session.refresh(new_toy)
        return new_toy

def get_toy(toy_id: int):
    with session_local() as session:
        toy = session.query(Toy).filter(Toy.id == toy_id).first()
        return toy 

def delete_toy(name):
    with session_local() as session:
        toy_to_delete = session.query(Toy).filter(Toy.name == name).first()

        if toy_to_delete:
            session.delete(toy_to_delete)
            session.commit()

def update_toy(toy_id: int, name: str, price: float, category: str, amount: int):
    with session_local() as session:
        toy = get_toy(toy_id)
        if not toy:
            return None

        toy.name = name
        toy.price = price
        toy.category = category
        toy.amount = amount
        session.add(toy)
        session.commit()

        return toy

def csv_to_db(data):
    with open(data, "r") as read:
        
        reading = csv.reader(read)
        for row in reading:
            new_toy = create_toy(name=row[0], price=row[1], category=row[2], amount=row[3])
            



csv_to_db("csv.csv")