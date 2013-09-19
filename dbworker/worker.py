import multiprocessing
import time
from datasource.engines import cybage
import os
from pymssql import Error
from logger.config import log


class DBWorker(multiprocessing.Process):

    def run(self):
        print 'Worker run() method for %s' % self.workerName
        log(' Starting DBWorker with process ID: ' + str(os.getpid()))
        try:
            for i in range(1, len(self.sql)):
                sql = self.sql[i]
                self.cur.execute(sql)
        except Error as e:
            log(' The process ' + str(os.getpid()) + ' encountered an error')
            log(str(e))

    def __init__(self, conn, *args, **kwargs):
        """
        Constructor for DBWorker.
        """
        super(DBWorker, self).__init__()
        self.sql = args
        self.num_args = len(args)
        self.conn = conn
        self.name = kwargs['name']
        self.workerName = multiprocessing.current_process().name
        self.cur = self.conn.getCursor()






