import psycopg2
from psycopg2.extensions import AsIs
from psycopg2.extras import DictCursor

import mysql.connector
from mysql.connector import errorcode

class Connection:
  def __init__(self, params, db_config, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.params = params
    self.db_config = db_config
    self.connection = None
  
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

class MySQLConnection(Connection):
  def connect(self):
    self.connection = mysql.connector.connect(
        user=self.params['user'],
        password=self.params['password'],
        host=self.params['host'],
        port=self.params['port'],
        database=self.params['dbname'])

  def cursor(self):
    return self.connection.cursor()

  def rollback(self):
      

class PostgreSQLConnection(Connection):
  def connect(self):
    self.connection = psycopg2.connect(' '.join(self.db_config))

  def cursor(self):
    return self.connection.cursor(cursor_factory=DictCursor)

  def rollback(self):
    self.connection.rollback()

'''
ALLOWED_CONFIG_PARAMS = ['user', 'dbname', 'password', 'host', 'port']
'''
def connection(db_config: list, auto_commit=False) -> Connection:
  params = {}
  for p in db_config:
    entry = p.split('=')
    params[entry[0]] = entry[1]    
  
  if params['adapter'] == 'mysql':
    connection = None
    try:
      connection = MySQLConnection(params=params, db_config=db_config)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Something is wrong with your user name or password')
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('Database does not exist')
      else:
        print(err)
    else:
      connection.close()
  else:
    try:
      connection = PostgreSQLConnection(params=params, db_config=db_config)
      connection.connection.autocommit = auto_commit
    except psycopg2.OperationalError as e:
      print('Unable to connect!\n{0}').format(e)
    else:
      print(err)
      connection.close()
   
  return connection

def cursor(con: Connection):
  return con.cursor()