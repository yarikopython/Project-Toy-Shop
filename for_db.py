import sqlite3
import csv
data = []
with open("csv.csv", "r") as csvfile:
    reader = csvfile.read()
    
    for x in reader:
        data.append(x)

con = sqlite3.connect("db.sqlite3")
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS my_table (
                category TEXT,
                name TEXT,
                amount BIGNINT,
                price BIGINT
             )''')

cursor.execute("""INSERT INTO my_table VALUES (data)""")

con.commit()

con.close()
