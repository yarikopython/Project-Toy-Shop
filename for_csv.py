from models import Toy
import csv

def spammreader():
    with open("csv.csv", "r") as reader:
        spammreader= csv.reader(reader)
        for x in spammreader:
            print(x)

spammreader()