from models import Toy
import csv

def spammreader(data):
    with open(data, "r") as reader:
        spammreader = csv.reader(reader)
        for x in spammreader:
            print(x)
            

spammreader("csv.csv")