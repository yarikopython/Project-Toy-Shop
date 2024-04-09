import csv

filepath = "csv.csv"
data = {"name": "yarik", "price": 2.0, "category": "gun", "amount": 11}


new_data = {
    "name": "guntoy",
    "price": 13.0,
    "category": "amount",
    "amount": "category",
}


def reader(filepath: str):
    try:
        with open(filepath, "r") as read:
            reader = csv.DictReader(read)
            for row in reader:
                print(row)
    except IOError:
        print(f"Error while reading {filepath}")


def write(filepath: str, data: dict):
    try:
        fieldnames = ["name", "price", "category", "amount"]
        with open(filepath, "w") as write:
            writer = csv.DictWriter(write, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)
    except FileNotFoundError:
        print(f"FIle {filepath} wasnt founded")


def updater(filepath: str, new_data: dict):
    try:
        write(filepath, new_data)
    except IOError:
        print(f"Error while updating data in {filepath}")
