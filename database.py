from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def create_database(url, base):
    engine = create_engine(url)
    base.metadata.create_all(engine)
    return engine


def create_session(engine):
    session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    session = session_local()
    return session


def format_for_csv(name: str, price: float,
                   category: str,
                   amount: str) -> dict:
    data_for_csv = {"name": name,
                    "price": price,
                    "category": category,
                    "amount": amount}
    return data_for_csv



