from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, Engine


def create_database(url, base) -> Engine:
    """[summary]
    Function create_database create database.

    Args:
        url (str): url link with the name of the new database.
        base (object): object of class Base.

    Returns:
        engine:  Sqlalchemy engine.
    """
    engine = create_engine(url)
    base.metadata.create_all(engine)
    return engine


def create_session(engine) -> Session:
    """[summary]
    Function create_session create session.

    Args:
        engine (object): Sqlalchemy engine.

    Returns:
        session: database session.
    """
    session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    session = session_local()
    return session


def format_for_csv(name: str, price: float,
                   category: str,
                   amount: str) -> dict:
    """[summary]
    Function format_for_csv format data for csv file.

    Args:
        name (str): name for future toy.
        price (float): price for future toy.
        category (str): category for future toy.
        amount (str): amount for future toy.

    Returns:
        dict: return dict with data of future toy.
    """
    data_for_csv = {"name": name,
                    "price": price,
                    "category": category,
                    "amount": amount}
    return data_for_csv



