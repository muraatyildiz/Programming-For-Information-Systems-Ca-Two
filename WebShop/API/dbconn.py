import sqlalchemy as sa
from sqlalchemy import create_engine
import urllib

conn_str = urllib.parse.quote_plus(
    'Data Source Name=KNITNETDS;'
    'Driver={SQL Server};'
    'Server=(localdb)\MSSQLLocalDB;' 
    'Database=;AdvancedDBFRI'
    'Trusted_connection=yes;'
)
 
try:
    
    ApiSQLEngine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn_str))
    print("Passed")
 
except:
    print("failed!")