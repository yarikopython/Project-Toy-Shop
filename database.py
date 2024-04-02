from work_with_csv import write, reader, updater
from models import Base, session, Toy, engine

Base.metadata.create_all(bind=engine)


def create_toy(name: str, price: float, category: str, amount: int):
    toy_with_name = session.query(Toy).filter(Toy.name == name).first()
    toys = session.query(Toy).all()
    if not toy_with_name:
        new_toy = Toy(name=name, price=price, category=category, amount=amount)
        toys_name = [toy.name for toy in toys]
        if new_toy.name not in toys_name:
            session.add(new_toy)
            session.commit()
            session.refresh(new_toy)
            return new_toy
    else:
        return "This toy already exists"


def get_toy(toy_id: int):
    toy = session.query(Toy).filter(Toy.id == toy_id).first()
    return toy


def delete_toy(name: str):
    toy_to_delete = session.query(Toy).filter(Toy.name == name).first()

    if toy_to_delete:
        session.delete(toy_to_delete)
        session.commit()
        return toy_to_delete
    else:
        return "Toy with this name is doesnt exist"


def update_toy(
    toy_id: int, name: str, price: float, category: str, amount: int
):
    toy = get_toy(toy_id)
    if toy:
        toy.name = name
        toy.price = price
        toy.category = category
        toy.amount = amount
        session.add(toy)
        session.commit()
        return toy
    else:
        return "Toy with this id doesnt exist"


def format_for_csv(
    name: str, price: float, category: str, amount: str
) -> dict:
    data_for_csv = {
        "name": name,
        "price": price,
        "category": category,
        "amount": amount,
    }
    return data_for_csv


def csv_to_db(filepath):
    try:
        read = reader(filepath)
        for row in read:
            create_toy(
                name=row["name"],
                price=row["price"],
                category=["category"],
                amount=row["amount"],
            )
    except TypeError as e:
        print(f"Error: {e}")
