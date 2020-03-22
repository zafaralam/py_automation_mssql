import pandas as pd
import pyodbc
import os
from config import CONN_STR, QUERY_PATH

cnxn = pyodbc.connect(CONN_STR)

def write_data():
    query = ""
    with open(os.path.join(QUERY_PATH, "script1.sql"), 'r') as file:
        query = file.read()

    tmp_df = pd.read_sql(query, cnxn)

    tmp_df.to_excel("Test.xlsx", index=False)

write_data()
