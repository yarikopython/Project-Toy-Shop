from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

url = "sqlite:///./db.sqlite3"
engine = create_engine(url)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = session_local()
Base = declarative_base()


class Toy(Base):
    __tablename__ = "toys"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float(precision=2), default=0.0)
    category = Column(String)
    amount = Column(Integer, default=0)
