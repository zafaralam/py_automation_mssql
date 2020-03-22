import pandas as pd
import pyodbc
import os
from config import CONN_STR, QUERY_PATH, GEN_FOLDER  # , logger
import logging
from comman import print_list_of_queries, get_list_of_avaiable_queries
# Get the logger specified in the file
logger = logging.getLogger(__name__)

A_EXPORT_TYPES = {
    1: "xlsx",
    2: "csv"
}


def write_data_to_file(script_name, filename, export_type):

    full_file_path = os.path.join(
        GEN_FOLDER, filename+"."+A_EXPORT_TYPES[export_type])
    try:
        with open(os.path.join(QUERY_PATH, script_name), 'r') as file:
            logger.info("Reading Script %s", script_name)
            query = file.read()
            with pyodbc.connect(CONN_STR) as cnxn:
                logger.debug("Running query \n %s", query)
                tmp_df = pd.read_sql(query, cnxn)
                if export_type == 1:
                    tmp_df.to_excel(full_file_path, index=False)
                elif export_type == 2:
                    tmp_df.to_csv(full_file_path, index=False)
                else:
                    pass
    except Exception as exception:
        logger.error("Error Saving file")


if __name__ == "__main__":
    available_queries = get_list_of_avaiable_queries()
    print("Hello, welcome to the Python MSSQL Extractor!")
    _exit = False
    while not _exit:
        print("\nPlease select from one of the following options")
        print("""
        1. List all available queries
        0. Exit
        """)
        user_input = input("Please enter your selection: ")

        try:
            user_input = int(user_input)

            # print("<======================================>\n")
            print("\n")

            if user_input < 0 or user_input > 1:
                print(
                    "Invalid selection, please select from one of the available options.")
            elif user_input == 0:
                print("Bye :), see you next time.")
                _exit = True
                exit(0)
            else:
                _in_query_selection = True
                user_query_selection = 0
                query_selected = False
                while _in_query_selection:
                    print("List of avaiable queries")
                    print_list_of_queries()
                    print("\t0) Back")

                    user_query_selection = input("Please select a query: ")

                    try:
                        user_query_selection = int(user_query_selection)

                        if user_query_selection < 0 or user_query_selection > len(available_queries.items()):
                            print("Invalid selection, please try again.")
                        elif user_query_selection == 0:
                            _in_query_selection = False
                        else:
                            _in_query_selection = False
                            query_selected = True
                    except Exception as file_exception:
                        print("Invalid selection, please try again.")
                if query_selected:
                    _in_export_type_selection = True
                    filename = ""
                    while _in_export_type_selection:
                        print("\nExport types avaiable")
                        print("\t1. Excel\n\t2. CSV\n\t0. Back")
                        export_type = input(
                            "Please select export type: ")
                        try:
                            export_type = int(export_type)
                            if export_type < 0 or export_type > 2:
                                print("Invalid selection, please try again")
                            elif export_type == 0:
                                _in_export_type_selection = False
                            elif export_type >= 1 and export_type <= 2:
                                filename = input(
                                    "Enter a filename, do not include the file extension:")
                                filename = filename.strip()
                                _in_export_type_selection = False
                            else:
                                _in_export_type_selection = False
                        except Exception as export_exception:
                            print("Invalid selection, please try again")

                    if export_type in A_EXPORT_TYPES:
                        write_data_to_file(
                            available_queries[user_query_selection], filename, export_type)

        except Exception as exception:
            print("Invalid selection, please select from one of the available options.")

    # print_list_of_queries()
