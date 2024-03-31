import csv
filepath = "toys.csv"
old_toy_name = "guntoy"
fieldnames = ["name", "price", "category", "amount"]
data = {
    "name":"yarik",
    "price":2.0,
    "category":"gun",
    "amount":11
    }


new_data = {
    "name":"guntoy",
    "price":13.0,
    "category":"amount",
    "amount":"category"
    }


def reader(filepath: str):
    with open(filepath, "r") as read:
        reader = csv.DictReader(read)
        for row in reader:
            print(row)      


def write(file : str, data: dict):
    with open(file, "w") as write:
        writer = csv.DictWriter(write,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(data)


def updater(filepath: str, new_data: dict):
    with open(filepath, "w") as update:
        write = csv.DictWriter(update, fieldnames=fieldnames)
        write.writeheader()
        write.writerow(new_data)


reader(filepath)
write(filepath, data)
updater(filepath, new_data)