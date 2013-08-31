import pymssql
import sys
from dbconfig import mssql
# sys.path.append("/home/coleman/Code/")


class MSSQLConnection(object):
    """
    Connection to MS SQL Server database.
    """
    def __init__(self):

        self.createConnection()

    def createConnection(self):

        try:
            self.con = pymssql.connect(host=mssql['host'], user=mssql['user'], 
                                password=mssql['password'], database=mssql['database'])
            print '[AlchemyConnection] Connection successful for user %s to database %s' % (mssql['user'],
                                                                                            mssql['database'])
        except pymssql.Error as e:
            pass

    def close(self):

        self.con.close()

    def getCursor(self):
        """
        Returns a pymssql cursor object. Call query methods on this cursor object.
        """
        self.cursor = self.con.cursor()
        return self.cursor  # returns pymssql cursor object

    def commit(self):

        self.con.commit()






"""
TODO remove this
Query methods for cursor objects:

cur.callproc       cur.executemany    cur.next           cur.setinputsizes
cur.close          cur.fetchall       cur.nextset        cur.setoutputsize
cur.connection     cur.fetchmany      cur.returnvalue    
cur.description    cur.fetchone       cur.rowcount       
cur.execute        cur.lastrowid      cur.rownumber

"""
