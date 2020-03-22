import pandas as pd
import pyodbc
import os
from config import CONN_STR, QUERY_PATH  # , logger
import logging

# Get the logger specified in the file
logger = logging.getLogger(__name__)


def write_data():
    with open(os.path.join(QUERY_PATH, "script1.sql"), 'r') as file:
        logger.info("Reading Script %s", "script1.sql")
        query = file.read()
        with pyodbc.connect(CONN_STR) as cnxn:
            tmp_df = pd.read_sql(query, cnxn)
            tmp_df.to_excel("Test.xlsx", index=False)


if __name__ == "__main__":
    write_data()
