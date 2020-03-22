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
_DATABASE = os.environ.get('DATABASE', 'master')
_USE_TRUSTED_CONN = os.environ.get('TRUSTED_CONN', "0")
_USERNAME = os.environ.get('DB_USERNAME', '')
_PASSWORD = os.environ.get('DB_PASSWORD', '')

CONN_STR = "DRIVER={ODBC Driver 17 for SQL Server};" + ("SERVER={0};DATABASE={1};Trusted_Connection=yes".format(_SERVER, _DATABASE) if _USE_TRUSTED_CONN == "1" else "SERVER={0};PORT=1433;DATABASE={1};UID={2};PWD={3}".format(
    _SERVER, _DATABASE, _USERNAME, _PASSWORD
))
# CONN_STR = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=AHDWDB01\\CDWH;DATABASE=CDWH;Trusted_Connection=yes"
# CONN_STR = "DRIVER={ODBC Driver 17 for SQL Server};SERVER={};PORT=1433;DATABASE={};UID={};PWD={}"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
QUERY_PATH = os.path.join(APP_ROOT, 'queries')


logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)

# Get the logger specified in the file
# logger = logging.getLogger(__name__)
