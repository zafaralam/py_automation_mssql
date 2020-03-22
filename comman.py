import os
import logging
from config import QUERY_PATH
# Get the logger specified in the file
logger = logging.getLogger(__name__)


def get_list_of_avaiable_queries():
    query_files = {}
    for path, dirs, files in os.walk(QUERY_PATH):
        for num, filename in enumerate(files):
            query_files[num] = filename

    return query_files


def print_list_of_queries():
    for key, val in get_list_of_avaiable_queries().items():
        print("\t{0}) {1}".format(key+1, val))
