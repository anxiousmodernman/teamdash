import pyodbc
import sys
from dbconfig import mssql_odbc_connection
# sys.path.append("/home/coleman/Code/")




class MSSQLConnection(object):
    """
    Connection to database.
    """
    def __init__(self):
        self.createConnection()

    def createConnection(self):
        try:
            self.con = pyodbc.connect('DSN=%s;UID=%s;PWD=%s' % (mssql_odbc_connection['dsn'], mssql_odbc_connection['UID'], mssql_odbc_connection['PWD']))
            print '[AlchemyConnection] Connection successful for user %s to database %s' % (mssql_odbc_connection['UID'], mssql_odbc_connection['dsn'])
        except pyodbc.DatabaseError as e:
            print 'Database connection failed.'
            pass

    def close(self):
        self.con.close()

    def commit(self):
        self.con.commit()

    def getCursor(self):
        self.cursor = self.con.cursor()
        return self.cursor  # returns pyodbc cursor object





"""
CURSOR METHODS

c.arraysize         c.executemany       c.nextset           c.rowVerColumns
c.close             c.fetchall          c.noscan            c.rowcount
c.columns           c.fetchmany         c.primaryKeys       c.setinputsizes
c.commit            c.fetchone          c.procedureColumns  c.setoutputsize
c.connection        c.foreignKeys       c.procedures        c.skip
c.description       c.getTypeInfo       c.rollback          c.statistics
c.execute           c.next              c.rowIdColumns      c.tables
"""






