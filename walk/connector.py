import psycopg2
from psycopg2.extensions import AsIs
from psycopg2.extras import DictCursor

import mysql.connector
from mysql.connector import errorcode

class Connection:
  def __init__(self, params, db_config, auto_commit, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.params = params
    self.db_config = db_config
    self.connection = None
    self.auto_commit = auto_commit
  
  def close(self):
    self.connection.close()

  def connect(self):
    pass

  def cursor(self):
    pass
  
  def commit(self):
    self.connection.commit()

  def rollback(self):
    pass  

  def database_exists(self, db_name):
    pass


class MySQLConnection(Connection):
  def connect(self):
    if self.auto_commit:
      self.connection = mysql.connector.connect(
        user=self.params['user'],
        passwd=self.params['password'] if 'password' in self.params else '',
        host=self.params['host'] if 'host' in self.params else 'localhost',
        port=self.params['port'] if 'port' in self.params else 3306)
      self.connection.autocommit = True
    else:
      self.connection = mysql.connector.connect(
        user=self.params['user'],
        passwd=self.params['password'] if 'password' in self.params else '',
        host=self.params['host'] if 'host' in self.params else 'localhost',
        port=self.params['port'] if 'port' in self.params else 3306,
        database=self.params['dbname'])
    return self

  def cursor(self):
    return self.connection.cursor(dictionary=True, buffered=True)
  
  def rollback(self):
    self.connection.rollback()

  def database_exists(self, db_name):
    cur = self.cursor()
    cur.execute('SHOW DATABASES')
    for d in cur:
      if d['Database'] == db_name:
        return True
    return False

class PostgreSQLConnection(Connection):
  def connect(self):
    if self.auto_commit:
      config = list(filter(lambda x: not x.startswith('adapter=') and not x.startswith('dbname='), self.db_config))
      self.connection = psycopg2.connect(' '.join(config))
      self.connection.autocommit = self.auto_commit
    else:
      config = list(filter(lambda x: not x.startswith('adapter='), self.db_config))
      self.connection = psycopg2.connect(' '.join(config))
      self.connection.autocommit = self.auto_commit
    return self

  def cursor(self):
    return self.connection.cursor(cursor_factory=DictCursor)

  def rollback(self):
    self.connection.rollback()
  
  def database_exists(self, db_name):
    cur = self.cursor()
    cur.execute('SELECT datname FROM pg_database')
    for d in cur:
      if d == db_name:
        return True
    return False

'''
ALLOWED_CONFIG_PARAMS = ['user', 'dbname', 'password', 'host', 'port']
'''
def connection(db_config: list, auto_commit=False) -> Connection:
  params = {}
  for p in db_config:
    entry = p.split('=')
    params[entry[0]] = entry[1]    
  
  if 'adapter' in params and params['adapter'] == 'mysql':
    connection = None
    try:
      connection = MySQLConnection(params=params, db_config=db_config, auto_commit=auto_commit).connect()
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Database does not exist')
      else:
        print(err)
      if connection:
        connection.close()
  else:
    try:
      connection = PostgreSQLConnection(params=params, db_config=db_config, auto_commit=auto_commit).connect()
    except psycopg2.OperationalError as e:
      print('Unable to connect!\n{0}').format(e)
      if connection:
        connection.close()
      
   
  return connection

def cursor(con: Connection):
  return con.cursor()