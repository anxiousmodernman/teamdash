from sqlalchemy import create_engine
from dbconfig import mssql_odbc_connection


def getMSSQLEngine():
    engine = create_engine('mssql+pyodbc://%s:%s@%s' %
                          (mssql_odbc_connection['UID'], mssql_odbc_connection['PWD'], mssql_odbc_connection['dsn']))
    return engine

