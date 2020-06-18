import os, json
from urllib import parse
from sqlalchemy import create_engine

class DBO:
    DBROOT = os.path.join(*[a for a in __file__.split('/') if len(a) > 0][:-2] + ['dbs'])
    dbname = 'elipsis.db'
    dsn = 'sqlite:////{}/{}'.format(DBROOT, dbname)

    def __init__(self):
        pass

    def dbo(self):
        return create_engine(self.dsn)
