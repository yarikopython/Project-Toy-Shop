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

read = reader(filepath)
tuple_data = [(), (), (), ()]
tuple_data[0] = read["name"]
tuple_data[1] = read["price"]
tuple_data[2] = read["category"]
tuple_data[3] = read["amount"]
print(tuple_data)

update_input = True


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
        id = Input(placeholder="Id", id="update_id", disabled=False)
        name = Input(
            placeholder="Name", id="update_name", disabled=update_input
        )
        price = Input(
            placeholder="Price", id="update_price", disabled=update_input
        )
        category = Input(
            placeholder="Category", id="update_category", disabled=update_input
        )
        amount = Input(
            placeholder="Amount", id="update_amount", disabled=update_input
        )
        update = Button("Update", id="update", disabled=update_input)
        check = Button("Check", id="check")
        return (id, name, price, category, amount, update, check)

    def menu_delete_toy(self):
        id = Input(placeholder="Id", id="id")
        delete = Button("Delete", id="delete")
        return (id, delete)

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("name", "price", "category", "amount")
        table.add_rows([tuple_data])

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create":
            inputs = self.query(Input)
            for i in inputs:
                if i.id == "create_name":
                    name = i.value
                elif i.id == "create_price":
                    price = i.value
                elif i.id == "create_category":
                    category = i.value
                elif i.id == "create_amount":
                    amount = i.value

            create_toy(name, price, category, amount)

        if event.button.id == "check":
            inputs = self.query(Input)


if __name__ == "__main__":
    app = ToyShop()
    app.run()
