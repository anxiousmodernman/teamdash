import unittest
from time import sleep
import sys
from dbworker import worker
from datasource.engines import *
import datetime


class DBWorkerTest(unittest.TestCase):

    def testDatabaseError(self):
        engine = getMSSQLEngine()
        conn = engine.connect()
        sleep(3)
        test_conn.close()

    # def testCreateTable(self):
    #     test_conn = CybageConnection()
    #     cur = test_conn.getCursor()
    #     cur.execute('CREATE TABLE ')
    #     test_conn.close()

    def testWorker(self):
        sql1 = 'select top 1 brief_name from brief'
        sql2 = 'select top 1 email from subscriber'
        conn = CybageConnection()
        w = worker.DBWorker(conn, sql1, sql2, name='testWorker')
        w.start()
        w.join()
        print '\nDone with testWorker()\n'




def main():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print 'Starting tests...\nTIMESTAMP ' + date
    unittest.main()

if __name__ == '__main__':
    main()