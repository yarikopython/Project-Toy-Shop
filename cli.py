from work_with_csv import write, reader, updater, filepath, data, new_data
from database import (
    delete_toy,
    create_toy,
    get_toy,
    update_toy,
    csv_to_db,
    format_for_csv,
)
from textual.app import App
from textual.widgets import Label, Input, Button


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


class ToyShop(App):
    def comprose(self):
        yield Label("ToyShop")
        yield Label("Work with  DB:")
        yield Button("Create toy")
        yield Button("Delete Toy")
        yield Button("Update Toy")
        yield Button("Get Toy")
        yield Label("Work with CSV")
        yield Button("Formating data for csv")
        yield Button("Write toy in csv")
        yield Button("Read toy from csv")
        yield Button("Update toy in csv")


if __name__ == "__main__":
    app = ToyShop()
    app.run()