
   # Assignment Day 7 - Python Database Connection Project which updates any one value in the table and select all the table data and print it.

import mysql.connector as sql           # importing module

# Connecting the local mysql database
database = sql.connect(host = 'localhost', user = 'root', passwd = 'water123', database = 'Info')

cur = database.cursor()


cur.execute("update student set Eng_mark = 95 where Roll_no = 103")     # Update the record 
cur.execute("select * from student")        # View the table

for i in cur:
    print(i)

cur.close()
database.commit() 