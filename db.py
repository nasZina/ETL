import pymysql
import csv
import os
from dotenv import load_dotenv
# runs at import time
load_dotenv()

# run at run time when function is called
def db_connect():
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")


    # Establish a database connection
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return connection

connection = db_connect()

# cursor = connection.cursor()
# cursor = connection.cursor(pymysql.cursors.DictCursor)

# Execute SQL query

def dict_reader(File_csv: str) -> list:

    dict_list=[]
    
    with open(File_csv +'.csv', 'r', newline='') as csvfile:
        
        reader = csv.DictReader(csvfile)

        #For later to return multiple returns
        #headers = reader.fieldnames

        for row in reader:
            dict_list.append(row)

        return dict_list #,headers
    
def check_data():
    # pseudocode
    # we have a sales.csv now stored in the computer memory as initial_records which is a list of dict
    # create a staging list =[]
    # iterate throught all dict list with a for loop
        # nested 2nd loop # for each key, value dictionary in initial_record var
        # read value and check for ' ' 
        # if value ==" ":
            # pass
        # else: add to new list created above
            # staging_list.append(this_row)
            
