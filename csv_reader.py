from models import Toy
import csv
def csv_reader(filepath: str):
    with open(filepath, "r") as read:
        reader = csv.reader(read)
        for x in reader:
            print(x)





def write(file : str, data: list):
        try:
            with open(file, "a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data)
        except FileNotFoundError:
            print("File format or file is not founded")

new_data = ["testt",100.1,"doll", 200]
def updater(filepath : str, name: str, new_data: str):
    with open(filepath, "r") as reader:
        read = csv.reader(reader)
        toys = list(read)
        for toy in toys:
            if  toy[0] == name:
                toy[1:] == new_data
    with open(filepath, "a") as update_write:
        writer = csv.writer(update_write)
        writer.writerows(toys)
write("csv.csv", ["testik", 2.0, "category", 200])
updater("csv.csv", "barbie", new_data)
