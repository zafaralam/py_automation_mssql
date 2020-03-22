import logging.config
import logging
import os
from pathlib import Path  # python3 only
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

_SERVER = os.environ.get('SERVER', 'localhost')
_DB_PORT = os.environ.get('DB_PORT', "1433")
_DATABASE = os.environ.get('DATABASE', 'master')
_USE_TRUSTED_CONN = os.environ.get('TRUSTED_CONN', "0")
_USERNAME = os.environ.get('DB_USERNAME', '')
_PASSWORD = os.environ.get('DB_PASSWORD', '')

CONN_STR = "DRIVER={SQL Server}"+";SERVER={0};PORT={1};DATABASE={2};".format(_SERVER, _DB_PORT, _DATABASE) + ("Trusted_Connection=yes" if _USE_TRUSTED_CONN == "1" else "UID={0};PWD={1}".format(
    _USERNAME, _PASSWORD
))
# CONN_STR = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=AHDWDB01\\CDWH;DATABASE=CDWH;Trusted_Connection=yes"
# CONN_STR = "DRIVER={ODBC Driver 17 for SQL Server};SERVER={};PORT=1433;DATABASE={};UID={};PWD={}"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
QUERY_PATH = os.path.join(APP_ROOT, 'queries')

GEN_FOLDER = os.path.join(APP_ROOT, 'generated')


logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)

# Get the logger specified in the file
# logger = logging.getLogger(__name__)
