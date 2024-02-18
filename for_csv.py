from models import Toy
import csv
objectik = Toy(input("Write a name of Toy: "),
               int(input("Write a price of Toy: ")),
               input("Write category of Toy: "), input("Write a amount of Toy: "))
listik = {
    "name":objectik.name,
    "price":objectik.price,
    "amount":objectik.amount,
    "category":objectik.category
}

    

def spammwriter():
    with open("csv.csv", "w", newline="") as writer:
        spammwriter = csv.writer(writer, delimiter="\n")
        spammwriter.writerow(f"Keys: {listik.keys}, Value: {listik.values}")

def spammreader():
    with open("csv.csv", "r") as reader:
        spammreader= csv.reader(reader)
        for x in spammreader:
            print(x)
try:
    while True:
        print("[1] - Write in csv ")
        inputik = int(input("What do you want to choose?: "))
        match inputik:
            case 1:
                spammwriter()
            case 2:
                spammreader()
            case 3:
                break
except FileNotFoundError:
    print("File is didnt founded")          