from models import Toy
import csv
def csv_reader(
        filepath: str, 
        format: list = ['name', 'price', 'amount', 'category'], 
        first_blank: bool = False
) -> list[list[str]] | str:
    try:
        with open(filepath) as file:
            csv_reader = csv.reader(file)
            data = list(csv_reader)
            
            if not first_blank:
                first_blank = format != data[0] 

            if first_blank:
                if len(data[0]) == len(format):
                    return data
            else:
                if data[0] == format:
                    return data[1:]
    
    except FileNotFoundError:
        return f'File {filepath} not found' 
    
    return ''
print(csv_reader("csv.csv"))