from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from database import create_database, create_session
from work_with_csv import reader

url = "sqlite:///./db.sqlite3"

Base = declarative_base()
db = create_database(url, Base)
session = create_session(db)

class Toy(Base):
    __tablename__ = "toys"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float(precision=2), default=0.0)
    category = Column(String)
    amount = Column(Integer, default=0)


def create_toy(session, name: str, price: float, category: str, amount: int):
    filter_name = session.query(Toy).filter(Toy.name == name).first()
    if not filter_name:
        new_toy = Toy(name=name, price=price,
                      category=category,
                      amount=amount)
        session.add(new_toy)
        session.commit()
        session.refresh(new_toy)
        
    else:
        return None
    return name

def get_toy(session, toy_id: int):
    toy = session.query(Toy).filter(Toy.id == toy_id).first()
    if not toy:
        return None
    return toy



def delete_toy(session, name):
    toy_to_delete = session.query(Toy).filter(Toy.name == name).first()
    if toy_to_delete:
        session.delete(toy_to_delete)
        session.commit()
        return toy_to_delete
    else:
        return None


def update_toy(session, toy_id, name: str, price: float, category: str, amount: int):
    toy = get_toy(session, toy_id)
    if toy:
        toy.name = name
        toy.price = price
        toy.category = category
        toy.amount = amount
        session.add(toy)
        session.commit()
        return toy
    else:
        return None

def csv_to_db(session, filepath):
    try:
        read = reader(filepath)
        for row in read:
            create_toy(session, name=row["name"],
                       price=row["price"],
                       category=row["category"],
                       amount=row["amount"])
    except TypeError as e:
        print(f"Error {e}")

Base.metadata.create_all(db)