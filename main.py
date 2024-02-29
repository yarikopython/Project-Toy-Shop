from database import session_local, Toy, csv_to_db
from csv_reader import spammreader

data = spammreader("csv.csv")
csv_to_db(data)

for toy in session_local().query(Toy).all():
    print(toy.name, toy.price, toy.category, toy.amount)

