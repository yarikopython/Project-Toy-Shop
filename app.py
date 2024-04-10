from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Label, Input, Button, DataTable
from work_with_csv import reader, write, updater, filepath
from database import create_toy, delete_toy, update_toy
read = reader(filepath)
tuple_data = [(), (), (), ()]
tuple_data[0] = read["name"]
tuple_data[1] = read["price"]
tuple_data[2] = read["category"]
tuple_data[3] = read["amount"]
print(tuple_data)
class ToyShop(App):
    CSS_PATH = "cli.tcss"
    def compose(self):
       yield Label("Data base of Toys:")
       yield DataTable()
       yield Label("Work with DB:")
       yield Button("")
       yield Button()
       yield Button()
       yield Button()
       yield Button()
       yield Button()
       yield Button()
       yield Button()
       
    
    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns("name", "price", "category", "amount")
        table.add_rows([tuple_data]) 
        
if __name__ == "__main__":
    app = ToyShop()
    app.run()