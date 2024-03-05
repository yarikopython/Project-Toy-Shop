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

def delete_toy():
    with session_local() as session:
        pass


def csv_to_db(data):
    with open(data, "r") as read:
        
        reading = csv.reader(read)
        for row in reading:
            new_toy = create_toy(name=row[0], price=row[1], category=row[2], amount=row[3])
            


Base.metadata.create_all(bind=engine)
csv_to_db("csv.csv")