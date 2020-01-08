

class Cursor:
  def __init__(self, cursor, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.cursor = cursor

  def execute(self, query, params=None):
    pass
  
  def table_exists(self, table_name):
    pass

class MySQLCursor(Cursor):
  def execute(self, query, params):
    pass

  def table_exists(self, table_name):
    pass

class PostgreSQLCursor(Cursor):
  def execute(self, query, params):
    pass

  def table_exists(self, table_name):
    pass    
