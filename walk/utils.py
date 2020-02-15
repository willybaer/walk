def sql_file_commands(file_content):
  sql_parts = file_content.split(';')
  for part in sql_parts:
    try:
      if part.strip() != '':
        yield part
    except IOError as e:
      print('Command skipped %s' % e)