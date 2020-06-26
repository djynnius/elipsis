import os, json
from urllib import parse
from sqlalchemy import create_engine

class DB:
    DBROOT = os.path.join(*[a for a in __file__.split('/') if len(a) > 0][:-2] + ['dbs'])
    dbname = 'elipsis.db'
    dsn = 'sqlite:////{}/{}'.format(DBROOT, dbname)

    def __init__(self):
        pass

    def dbo(self):
        '''Connector for SQLite3 DB in app. Good for config and settings'''
        return create_engine(self.dsn)

    #SQLite3
    def sqlite(self):
        '''Alias for dbo'''
        return create_engine(self.dsn)

    def sqlite3(self):
        '''Alias for dbo'''
        return create_engine(self.dsn)

    #MariaDB/MySQL
    def maria(self, user, passwd, db, port=3306, host='localhost'):
        '''MySQL/MariaDB connector'''
        dsn = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(user, parse.quote(passwd), host, port, db)
        return create_engine(dsn)

    def my(self, user, passwd, db, port=3306, host='localhost'):
        '''alias for maria'''
        return self.maria(user, passwd, db, port, host)

    def mariadb(self, user, passwd, db, port=3306, host='localhost'):
        '''alias for maria'''
        return self.maria(user, passwd, db, port, host)

    def mysql(self, user, passwd, db, port=3306, host='localhost'):
        '''alias for maria'''
        return self.maria(user, passwd, db, port, host)

    #PostgreSQL
    def postgres(self, user, passwd, db, port=5432, host='localhost'):
        '''PostgreSQL connector'''
        dsn = 'postgres://{0}:{1}@{2}:{3}/{4}'.format(user, parse.quote(passwd), host, port, db)
        return create_engine(dsn)

    def pg(self, user, passwd, db, port=5432, host='localhost'):
        '''PostgreSQL connector alias'''
        return self.postgres(user, passwd, db, port, host)

    def pgsql(self, user, passwd, db, port=5432, host='localhost'):
        '''PostgreSQL connector alias'''
        return self.postgres(user, passwd, db, port, host)

    #MicrosoftSQL
    def ms(self, passwd, db, user='sa', port=1433, host='localhost'):
        '''Microsoft SQL connector'''
        dsn = 'mssql+pymssql://<username>:<password>@<freetds_name>/?charset=utf8'
        return create_engine(dsn)

    #Oracle
    def oracle(self, user, passwd, db, port=4333, host='localhost'):
        '''Oracle connector'''
        dsn = 'oracle+cx_oracle://{}:{}@{}:{}/{}?encoding=UTF-8&nencoding=UTF-8'.format(user, parse.quote(passwd), host, port, db)
        return create_engine(dsn)

    #MongoDB
    def mongo(self, user, passwd, db, port=27027, host='localhost'):
        '''MongoDB connector'''
        dsn = ''.format(user, parse.quote(passwd), host, port, db)
        return create_engine(dsn)
