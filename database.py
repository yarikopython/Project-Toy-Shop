from csv_reader import write, reader, updater
from models import Base, toys, session, csv_toy, Toy, engine

Base.metadata.create_all(bind=engine)
            
def create_toy(name: str, price: float, category: str, amount: int):
        new_toy = Toy(name=name, price=price, category=category, amount=amount)
        toys_name = [toy.name for toy in toys]
        if new_toy.name not in toys_name:
            session.add(new_toy)
            session.commit()
            session.refresh(new_toy)
            
        new_toy

def get_toy(toy_id: int):
        toy = session.query(Toy).filter(Toy.id == toy_id).first()
        print(toy) 
        return toy

def delete_toy(name):
        toy_to_delete = session.query(Toy).filter(Toy.name == name).first()

        if toy_to_delete:
            session.delete(toy_to_delete)
            session.commit()
        
        return toy_to_delete
def update_toy(toy_id, list_of_inputs):
        toy = get_toy(toy_id)
        if not toy:
            return None

        toy.name = list_of_inputs[0]
        toy.price = list_of_inputs[1]
        toy.category = list_of_inputs[2]
        toy.amount = list_of_inputs[3]
        session.add(toy)
        session.commit()
        csv_toy.append(toy)

        return toy

def format_for_csv(name: str, price: float, category: str, amount: str) -> list:
    data_for_csv = []
    for toys_list in (name, price, category, amount):
        data_for_csv.append(toys_list)
        write("csv.csv", data_for_csv)
    return data_for_csv

def csv_to_db(file):
        reader(file)
        for row in reader:
            new_toy = create_toy(name=row[0], price=row[1],category=[2], amount=row[3])



csv_to_db("csv.csv")
