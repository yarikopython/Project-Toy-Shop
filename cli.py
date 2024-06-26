from work_with_csv import write, reader, updater, filepath, data, new_data
from models import (
    delete_toy,
    create_toy,
    get_toy,
    update_toy,
    csv_to_db

)
from database import format_for_csv


def main():
    new_toy_data = {
        "name": "nerf blasser",
        "price": 19.5,
        "category": "blaser",
        "amount": 90,
    }
    toy_to_delete = "nerf blaster"
    toy_to_update_id = 1
    toy_to_update = {
        "name": "gun machine",
        "price": 10.9,
        "category": "machinegun",
        "amount": 90,
    }
    data_for_csv_format = {
        "name": "pokemon",
        "price": 30.0,
        "category": "pokemon",
        "amount": 50,
    }

    # functions for work with sqiite3 data base

    create_toy(
        name=new_toy_data["name"],
        price=new_toy_data["price"],
        category=new_toy_data["category"],
        amount=new_toy_data["amount"],
    )
    delete_toy(toy_to_delete)
    update_toy(
        toy_id=toy_to_update_id,
        name=toy_to_update["name"],
        price=toy_to_update["price"],
        category=toy_to_update["category"],
        amount=toy_to_update["amount"],
    )
    get_toy(toy_to_update_id)
    format_for_csv(
        name=data_for_csv_format["name"],
        price=data_for_csv_format["price"],
        category=data_for_csv_format["category"],
        amount=data_for_csv_format["amount"],
    )

    csv_to_db(filepath)

    # parameters for csv-work functions

    write(filepath=filepath, data=data)
    reader(filepath=filepath)
    updater(filepath=filepath, new_data=new_data)
