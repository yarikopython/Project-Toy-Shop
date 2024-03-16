from pytermgui  import *
#from database import delete_toy, create_toy, get_toy, session_local, Toy
options = ["\nNew toy,\ndelete toy,\nget toy"]
def menu():
    w = Window(title="Menu")
    w.set_title("Toy Shop")
    w.Menu()
    w.build()

"""def new_toy(name: str, price: float, category: str, amount: int):
    create_toy(name, price, category, amount)
    

def delete_the_toy(name):
    delete_toy(name)
    

def get_toy(toy_id: int):
    with session_local() as session:
        toy = session.query(Toy).filter(Toy.id == toy_id).first()
        return toy """


if __name__ == "__main__":
    menu()


