from models import Toy
import csv
objectik = Toy(input("Write a name of Toy: "),
               int(input("Write a price of Toy: ")),
               input("Write category of Toy: "), input("Write a amount of Toy: "))
listik = [
    objectik.name,
    objectik.price,
    objectik.amount,
    objectik.category
]

with open("csv.csv", "w", newline="") as writer:
    spammwriter = csv.writer(writer, delimiter="\n")
    spammwriter.writerow(listik)
with open("csv.csv", "r") as reader:
    spammreader= csv.reader(reader)
    for x in spammreader:
        print(x)

    