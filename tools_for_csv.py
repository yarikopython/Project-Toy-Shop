import csv
filepath = "toys.csv"
old_toy_name = "guntoy"
data = {
    "name":"dididon",
    "price":2.0,
    "category":"gun",
    "amount":22
    }
loaded_data = {}
def reader(filepath: str):
    with open(filepath, "r") as read:
        reader = csv.DictReader(read)
        for x in reader:
            return x

def write(file : str, data: dict):
    with open(file, "w") as write:
        writer = csv.DictWriter(write,fieldnames=["name", "price", "category", "amount"])
        writer.writeheader()
        for row in data:
            writer.writerow(data[row])


def updater(filepath: str, old_name: str, new_data: dict):

#update_toy(filepath, old_toy_name, data)