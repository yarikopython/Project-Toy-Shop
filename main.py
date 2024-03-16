import typer

from database import session_local, Toy, csv_to_db, create_toy, delete_toy, update_toy
from csv_reader import spammreader

app = typer.Typer()

@app.callback(invoke_without_command=True)
def run():
    csv_to_db(spammreader("csv.csv"))
    print("Initializing database")

@app.command("create")
def create(name: str, price: float, category: str, amount: int):
    create_toy(name, price, category, amount)
    print(f"Created toy {name}")

@app.command("delete")
def delete(toy_id: int):
    toy = delete_toy(toy_id)
    if not toy:
        print(f"Toy with id {toy_id} not found")
    else:
        print(f"Deleted toy {toy.name}")

@app.command()
def update(toy_id: int, name: str, price: float, category: str, amount: int):
    toy = update_toy(toy_id, name, price, category, amount)
    if not toy:
        print(f"Toy with id {toy_id} not found")
    else:
        print(f"Updated toy {toy.name}")

if __name__ == "__main__":
    app()