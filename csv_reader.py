import csv

def spammreader(filename):
    with open(filename, "r") as reader:
        spammreader = csv.reader(reader)
        data = []
        for row in spammreader:
            data.append(row)
    return data[1:]


