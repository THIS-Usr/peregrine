from __future__ import print_function
import pymysql
# import mysql.connector #instead of MySQLdb
# import mysqlclient # To use MySQL-Python on Python 3, they recommend a fork of it, mysqlclient
# from anaconda I have mysql, msql-connector-c, myswql-connector-python, mysqlclient but uncertain about this
# as in preferences list but not found here, and sqlacademy
# URI = 'mysql+mysqlconnector://$USER:$PASS@$HOST/$DB'

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='mentrandr', db='asperegrine')

cur = conn.cursor()
cur.execute("SELECT * FROM asperegrine.test_table where 1")

print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()

import urllib.request
import numpy as np
import mysql.connector as mysql

from datetime import date, datetime, timedelta



cnx = mysql.connect(user='root', password='mentrandr', database='asperegrine')

cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

id= cursor.lastrowid

add_row = ("INSERT INTO test_table"
                "(id, first, last)"
               "VALUES(%s, %s, %s)")

row_data = (id, 'adam', 'adams')

cursor.execute(add_row, row_data)

cnx.commit()

cursor.close()
cnx.close()

# mysqlclient (a maintained fork of MySQL-Python)
# engine = create_engine('mysql+mysqldb://scott:tiger@localhost/foo')

# PyMySQL
# engine = create_engine('mysql+pymysql://scott:tiger@localhost/foo')


import sqlalchemy as sql
import pandas as pd

# for mysql:////myapp:password@localhost/mydatabase?auth_plugin=mysql_native_password
# connect_string = 'mysql://root:mentrandr@localhost/asperegrine?auth_plugin=mysql_native_password' KO

# connect_string = 'mysql+mysqldb://root:mentrandr@localhost/asperegrine' KO

connect_string = 'mysql+pymysql://root:mentrandr@localhost/asperegrine' # OK

sql_engine = sql.create_engine(connect_string)

query =query = "select * from test_table"
df = pd.read_sql_query(query, sql_engine)

print(df)
