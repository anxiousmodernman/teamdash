"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
# import unittest
from mssql import MSSQLConnection
from engines import getMSSQLEngine
import unittest


class MSSQLDatabaseTest(TestCase):

    def testConnection(self):
        engine = getMSSQLEngine()
        conn = engine.connect()
        result_proxy = conn.execute("select brief_name from brief where brief_name = 'AAAA'")
        result = [item['brief_name'] for item in result_proxy]
        self.assertEquals(result, ['AAAA'])
        conn.close()



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

# if __name__ == '__main__':
#     unittest.main()