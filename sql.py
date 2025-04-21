import sqlite3
## connect to sqlite
connection=sqlite3.connect("student.db")

##create a cursor  to insert a recort ,create a table,retrieve

cursor=connection.cursor()

## create the table
table_info = '''
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
'''

cursor.execute(table_info)

##insert Some more recorrds
cursor.execute('''INSERT INTO STUDENT VALUES('Aarav Mehta', '10', 'A', 88)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Isha Sharma', 'Data Science', 'B', 92)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Rohan Patel', 'Data Science', 'C', 76)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sneha Verma', '11', 'A', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Karan Gupta', 'Data Science', 'B', 90)''')



## Display all the records
print("all the inserted records are")

data=cursor.execute(''' select * from STUDENT''')

for row in data:
    print(row)

##close the connection
connection.commit()
connection.close()
