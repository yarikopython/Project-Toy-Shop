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
    "category": "gun",
    "amount": 12
    }
file_not_found_dict = {}


def reader(filepath: str):
    result = []
    with open(filepath, "r") as read:
        reader = csv.reader(read)
        for row in reader:
                if len(row):
                    result_row = {}
                    result_row["name"] = row[0]
                    result_row["price"] = float(row[1])
                    result_row["category"] = row[2]
                    result_row["amount"] = float(row[3])
                    result.append(result_row)   
        return result


def write(filepath: str, data: dict):
    try:
        with open(filepath, "w", newline="") as write:
            writer = csv.writer(write)
            if data:
                data = [value for value in data.values()]
                writer.writerow(data)
                return data
    except AttributeError as e:
        print(f"Error: {e}")


def updater(filepath: str, new_data: dict) -> None:
    try:
        write(filepath, new_data)     
        return new_data
    except AttributeError as e:
        print(f"Error: {e} you must to write dict not str")