from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import (
    Label,
    Input,
    Button,
    DataTable,
    Input,
    TabbedContent,
    TabPane,
)
from work_with_csv import reader, write, updater, filepath
from database import create_toy, delete_toy, update_toy, get_toy
from models import toys
tuple_data = []

for toy in toys:
    tuple_data.append((toy.id,toy.name,toy.price,toy.category, toy.amount))

update_input = True
delete_input = True

class ToyShop(App):
    CSS_PATH = "cli.tcss"

    def compose(self):
        yield Label("Data base of Toys:")
        yield DataTable()
        yield Label("Work with DB:")
        with TabbedContent():
            with TabPane("Create Toy"):
                for i in self.menu_create_toy():
                    yield i

            with TabPane("Update Toy"):
                for i in self.menu_update_toy():
                    yield i

            with TabPane("Delete Toy"):
                for i in self.menu_delete_toy():
                    yield i

    def menu_create_toy(self):
        name = Input(placeholder="Name", id="create_name")
        price = Input(placeholder="Price", id="create_price")
        category = Input(placeholder="Category", id="create_category")
        amount = Input(placeholder="Amount", id="create_amount")
        create = Button("Create", id="create")
        return (name, price, category, amount, create)

    def menu_update_toy(self):
        id = Input(placeholder="Id", id="update_id")
        name = Input(
            placeholder="Name", id="update_name"
        )
        price = Input(
            placeholder="Price", id="update_price"
        )
        category = Input(
            placeholder="Category", id="update_category"
        )
        amount = Input(
            placeholder="Amount", id="update_amount"
        )
        update = Button("Update", id="update")
        return (id, name, price, category, amount, update)


    def menu_delete_toy(self):
        name = Input(placeholder="name", id="delete_name")
        delete = Button("Delete", id="delete")
        
        return (name, delete)

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("id", "name", "price", "category", "amount")
        table.add_rows(tuple_data)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create":
            inputs = self.query(Input)
            for create in inputs:
                if create.id == "create_name":
                    name = create.value
                elif create.id == "create_price":
                    price = create.value
                elif create.id == "create_category":
                    category = create.value
                elif create.id == "create_amount":
                    amount = create.value
            create_toy(name,price,category,amount)
        if event.button.id == "update":
            inputs = self.query(Input)
            for update in inputs:
                if update.id == "update_id":
                    id = update.value
                elif update.id == "update_name":
                    name = update.value
                elif update.id == "update_price":
                    price = update.value
                elif update.id == "update_category":
                    category = update.value
                elif update.id == "update_amount":
                    amount = update.value
            update_toy(id, name, price, category, amount)
        
        if event.button.id == "delete":
            inputs = self.query(Input)
            for delete in inputs:
                    name = delete.value
                    delete_toy(name)
                


if __name__ == "__main__":
    app = ToyShop()
    app.run()