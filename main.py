import pandas as pd
import pyodbc
import os
from config import CONN_STR, QUERY_PATH  # , logger
import logging
from comman import print_list_of_queries
# Get the logger specified in the file
logger = logging.getLogger(__name__)


def write_data_to_excel():
    with open(os.path.join(QUERY_PATH, "script1.sql"), 'r') as file:
        logger.info("Reading Script %s", "script1.sql")
        query = file.read()
        with pyodbc.connect(CONN_STR) as cnxn:
            logger.debug("Running query \n %s", query)
            tmp_df = pd.read_sql(query, cnxn)
            tmp_df.to_excel("Test.xlsx", index=False)


def write_data_to_csv():
    with open(os.path.join(QUERY_PATH, "script1.sql"), 'r') as file:
        logger.info("Reading Script %s", "script1.sql")
        query = file.read()
        with pyodbc.connect(CONN_STR) as cnxn:
            logger.debug("Running query \n %s", query)
            tmp_df = pd.read_sql(query, cnxn)
            tmp_df.to_csv("Test.csv", index=False)


if __name__ == "__main__":
    print_list_of_queries()
