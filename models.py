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
    """[summary]
    Function creating toy and add it to database.

    Args:
        session (Session): Sqlalchemy session.
        name (str): name for toy.
        price (float): price for toy.
        category (str): category for toy.
        amount (int): amount for toy.

    Returns:
        str: name for toy.
    """
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
    """[summary]
    Function for get toy from database
    
    Args:
        session (Session): Sqlachemy session.
        toy_id (int): id from toy.

    Returns:
        Toy: object class Toy. 
    """
    toy = session.query(Toy).filter(Toy.id == toy_id).first()
    if not toy:
        return None
    return toy



def delete_toy(session, name):
    """[summary]
    function that delete toy from database.
    
    Args:
        session (Session): Sqlalchemy session.
        name (str): toy name that will be delete.

    Returns:
        Toy: object class Toy.
    """
    toy_to_delete = session.query(Toy).filter(Toy.name == name).first()
    if toy_to_delete:
        session.delete(toy_to_delete)
        session.commit()
        return toy_to_delete
    else:
        return None


def update_toy(session, toy_id: int, name:
    str, price:
    float, category:
    str, amount: int):
    """[summary]
    function that update toy from database.

    Args:
        session (Session): Sqlalchemy session.
        toy_id (int): toy id that will be update.
        name (str): name for new toy.
        price (float): price for new toy.
        category (str): category for new toy.
        amount (int): amount for new toy.

    Returns:
        Toy: object class Toy
    """
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
    """[summary]
    function that get data from *.csv file, and create toy with this data.

    Args:
        session (Session): Sqlachemy session.
        filepath (str): filepath to *.csv file.

    Returns:
        list: data from *.csv file
    """
    try:
        read = reader(filepath)
        for row in read:
            create_toy(session, name=row["name"],
                       price=row["price"],
                       category=row["category"],
                       amount=row["amount"])
            return row
    except TypeError as e:
        print(f"Error {e}")

Base.metadata.create_all(db)