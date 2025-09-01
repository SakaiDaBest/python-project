import sqlite3
import pandas as pd

conn = sqlite3.connect('INSTRUCTOR.db')
cursor_obj = conn.cursor()
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")
table = """CREATE TABLE 
IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL,FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""

cursor_obj.execute(table)
print("Table is ready")

cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA'),(2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')

statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)

# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)

df = pd.read_sql_query("SELECT * FROM INSTRUCTOR;", conn)
df
df.shape
conn.close()