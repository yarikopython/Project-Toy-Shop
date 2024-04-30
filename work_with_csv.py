import csv
filepath = "csv.csv"
data = {
    "name": "yarik",
    "price": 2.0,
    "category": "gun",
    "amount": 11
    }


new_data = {
    "name": "guntoy",
    "price": 13.0,
    "category": "amount",
    "amount": "category"
    }


def reader(filepath: str):
    try:
        with open(filepath, "r") as read:
            result = []
            result_row = {}
            reader = csv.reader(read)
            for row in reader:
                result_row["name"] = row[0]
                result_row["price"] = float(row[1])
                result_row["category"] = row[2]
                result_row["amount"] = float(row[3])
                result.append(result_row)
            return result
    except IOError:
        print(f"Error while reading {filepath} or {filepath} doesnt exists.")


def write(filepath: str, data: dict):
    try:
        fieldnames = ["name", "price", "category", "amount"]
        with open(filepath, "w") as write:
            writer = csv.DictWriter(write, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)
    except IOError:
        print(f"Error while writing data in {filepath}")


def updater(filepath: str, new_data: dict):
    try:
        write(filepath, new_data)
    except IOError:
        print(f"Error while updating data in {filepath}")