import pyodbc
import sys
from dbconfig import mssql_connection
# sys.path.append("/home/coleman/Code/")




class MSSQLConnection(object):
    """
    Connection to database.
    """
    def __init__(self):

        self.createConnection()

    def createConnection(self):

        try:
            self.con = pyodbc.connect('DSN=%s;UID=%s;PWD=%s' % (mssql_connection['dsn'], mssql_connection['UID'], mssql_connection['PWD']))
            print '[AlchemyConnection] Connection successful for user %s to database %s' % (mssql_connection['UID'], mssql_connection['dsn'])
        except pyodbc.DatabaseError as e:
            print 'Database connection failed.'
            pass

    def close(self):

        self.con.close()

    def getCursor(self):
        self.cursor = self.con.cursor()
        return self.cursor  # returns pyodbc cursor object

    def commit(self):

        self.con.commit()






