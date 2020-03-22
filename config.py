import os

# CONN_STR = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=AHDWDB01\\CDWH;DATABASE=CDWH;Trusted_Connection=yes"
CONN_STR = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=172.28.128.6;PORT=1433;DATABASE=Scorecards;UID=scorecard;PWD=scorecard01"
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
QUERY_PATH = os.path.join(APP_ROOT, 'queries')