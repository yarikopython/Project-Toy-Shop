from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

url = "sqlite:///./db.sqlite3"
Base = declarative_base()
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


class Toy(Base):
    __tablename__ = "toys"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float(precision=2), default=0.0)
    category = Column(String)
    amount = Column(Integer, default=0)


Base.metadata.create_all(engine)
toys = session.query(Toy).all()
