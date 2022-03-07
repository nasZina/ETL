import csv
from pprint import pp

import db 

# extract from sales.csv

initial_records = db.dict_reader("sales")
print(initial_records)