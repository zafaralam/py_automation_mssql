import pandas as pd
import pyodbc
import os
from config import APP_ROOT, CONN_STR, QUERY_PATH, GEN_FOLDER  # , logger
import logging
from comman import print_list_of_queries, get_list_of_avaiable_queries
# Get the logger specified in the file
logger = logging.getLogger(__name__)

A_EXPORT_TYPES = {
    1: "xlsx",
    2: "csv"
}


def setup():

    if not os.path.isfile(os.path.join(APP_ROOT, ".env")):
        server = input("Enter server name: ")
        port = input("Enter port number (Default 1433): ")
        database = input("Enter database name: ")
        trusted_conn = input("Use trusted connection (y/n): ")

        if trusted_conn != "y":
            trusted_conn = 0
            username = input("Enter database username: ")
            password = input("Enter database password: ")
        else:
            trusted_conn = 1
            username = ""
            password = ""
        with open(os.path.join(APP_ROOT, ".env"), "w") as file:

            file.writelines(
                ["SERVER={0}\n".format(server), "DATABASE={0}\n".format(database), "DB_PORT={0}\n".format(port), "TRUSTED_CONN={0}\n".format(trusted_conn),
                    "DB_USERNAME={0}\n".format(username), "DB_PASSWORD={0}\n".format(password)],
            )
        # add file

    if not os.path.isdir(GEN_FOLDER):
        os.mkdir(GEN_FOLDER)

    if not os.path.isdir(QUERY_PATH):
        os.mkdir(QUERY_PATH)


def write_data_to_file(script_name, filename, export_type):

    full_file_path = os.path.join(
        GEN_FOLDER, filename+"."+A_EXPORT_TYPES[export_type])
    try:
        with open(os.path.join(QUERY_PATH, script_name), 'r') as file:
            logger.info("Reading Script %s", script_name)
            query = file.read()
            query = "SET NOCOUNT ON;\n{0}\nSET NOCOUNT OFF;".format(query)
            with pyodbc.connect(CONN_STR) as cnxn:
                logger.info("Running query \n %s", query)
                tmp_df = pd.read_sql(query, cnxn)
                if export_type == 1:
                    tmp_df.to_excel(full_file_path, index=False)
                elif export_type == 2:
                    tmp_df.to_csv(full_file_path, index=False)
                else:
                    pass
        print("Your exported file is: ", full_file_path)
    except Exception as exception:
        logger.exception("Error Saving file", exc_info=True)


def program():
    setup()
    available_queries = get_list_of_avaiable_queries()
    if len(available_queries.items()) == 0:
        print("""
No queries found, please place your queries in the 'quries' folder within the project and
run the program.
""")
        exit(0)
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
                raise Exception(
                    "Invalid main menu selection {0}".format(user_input))
            elif user_input == 0:
                print("Bye :) see you next time.")
                _exit = True
                exit(0)
            else:
                _in_query_selection = True
                user_query_selection = 0
                query_selected = False
                while _in_query_selection:
                    print("List of avaiable queries")
                    print_list_of_queries()
                    print("\t0) <-- Back")

                    user_query_selection = input("Please select a query: ")

                    try:
                        user_query_selection = int(user_query_selection)

                        if user_query_selection < 0 or user_query_selection > len(available_queries.items()):
                            # print(", please try again.")
                            raise Exception(
                                "Invalid query selection {0}".format(user_query_selection))
                        elif user_query_selection == 0:
                            _in_query_selection = False
                        else:
                            _in_query_selection = False
                            query_selected = True
                    except Exception as file_exception:
                        logger.exception(
                            "Error selecting query", exc_info=True)
                if query_selected:
                    _in_export_type_selection = True
                    filename = ""
                    while _in_export_type_selection:
                        print("\nExport types avaiable")
                        print("\t1. Excel\n\t2. CSV\n\t0. <-- Back")
                        export_type = input(
                            "Please select export type: ")
                        try:
                            export_type = int(export_type)
                            if export_type < 0 or export_type > 2:
                                raise Exception(
                                    "Invalid export type selection {0}".format(A_EXPORT_TYPES[export_type]))
                            elif export_type == 0:
                                _in_export_type_selection = False
                            elif export_type >= 1 and export_type <= 2:
                                filename = input(
                                    "Enter a filename, do not include the file extension: ")
                                filename = filename.strip()
                                _in_export_type_selection = False
                            else:
                                _in_export_type_selection = False
                        except Exception as export_exception:
                            logger.exception(
                                "Error selecting export type", exc_info=True)

                    if export_type in A_EXPORT_TYPES:
                        write_data_to_file(
                            available_queries[user_query_selection], filename, export_type)

        except Exception as exception:
            logger.exception(
                "Error selecting main menu", exc_info=True)


if __name__ == "__main__":
    program()
