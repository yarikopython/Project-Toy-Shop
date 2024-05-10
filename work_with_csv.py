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


def reader(filepath: str) -> list:
    """[summary]
    Function reader read the *.csv file and return data as list of
    dicts for every row. 
    

    Args:
        filepath (str): filepath to *.csv file.

    Returns:
        list: return whole data as list. 
    """
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


def writer(filepath: str, data: dict) -> list:
    """[summary]
    Function writer write data in *.csv file.

    Args:
        filepath (str): filepath to *.csv file.
        data (dict): data that will be write in *.csv file.

    Returns:
        list: return data as list of every row.
    
    Excepting:
        AttributeError: if data is empty.
    """
    try:
        with open(filepath, "w", newline="") as write:
            writer = csv.writer(write)
            if data:
                data = [value for value in data.values()]
                writer.writerow(data)
                return data
    except AttributeError as e:
        print(f"Error: {e}")


def updater(filepath: str, new_data: dict) -> dict:
    """[summary]
    Function updater update data in *.csv file.
    
    Args:
        filepath (str): filepath to *.csv file.
        new_data (dict): data that will be update old data in *.csv file.

    Returns:
        dict: return data.
    
    Excepting:
        AttributeError: if data is empty.
    """
    try:
        writer(filepath, new_data)
        
    except AttributeError as e:
        print(f"Error: {e}")