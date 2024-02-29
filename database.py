from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float


url = "sqlite:///./db.sqlite3"
engine = create_engine(url)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Toy(Base):
    __tablename__ = "toys"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float(precision=2), default=0.0)
    category = Column(String)
    amount = Column(Integer, default=0)
    
        
def create_toy(name: str, price: float, category: str, amount: int):
    with session_local() as session:
        new_toy = Toy(name=name, price=price, category=category, amount=amount)
        toys = session_local().query(Toy).all()
        toys_name = [toy.name for toy in toys]
        if new_toy.name not in toys_name:
            session.add(new_toy)
            session.commit()
            session.refresh(new_toy)
        return new_toy


def csv_to_db(data):
    for row in data:
        new_toy = create_toy(name=row[0], price=row[1], category=row[2], amount=row[3])
    return new_toy

Base.metadata.create_all(bind=engine)

# data = []
# with open("csv.csv", "r") as csvfile:
#     reader = csvfile.read()
    
#     for x in reader:
#         data.append(x)

# con = sqlite3.connect("db.sqlite3")
# cursor = con.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
#                 category TEXT,
#                 name TEXT,
#                 amount BIGNINT,
#                 price BIGINT
#              )''')

# cursor.execute("""INSERT INTO my_table VALUES (data)""")

# con.commit()

# con.close()
