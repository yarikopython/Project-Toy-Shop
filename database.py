from models import Toy, session
from work_with_csv import reader


def create_toy(name: str, price: float, category: str, amount: int):
    filter_name = session.query(Toy).filter(Toy.name == name).first()
    if not filter_name:
        new_toy = Toy(name=name, price=price,
                      category=category,
                      amount=amount)
        session.add(new_toy)
        session.commit()
        session.refresh(new_toy)
    else:
        print("this toy is already exist")


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
    else:
        print("Toy with this name does not exist")


def update_toy(toy_id, name: str, price: float, category: str, amount: int):
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
        return None


def format_for_csv(name: str, price: float,
                   category: str,
                   amount: str) -> dict:
    data_for_csv = {"name": name,
                    "price": price,
                    "category": category,
                    "amount": amount}
    print(data_for_csv)


def csv_to_db(filepath):
    try:
        read = reader(filepath)
        for row in read:
            create_toy(name=row["name"],
                    price=row["price"],
                    category=row["category"],
                    amount=row["amount"])
    except TypeError as e:
        print(f"Error {e}")