import sqlite3
import pandas as pd
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
sales = pd.read_csv(r"/Users/aravind/Downloads/100 Sales Records.csv")
print(sales)

# cursor.execute('''CREATE TABLE SCHOOL
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          MARKS          INT);''')
#
# cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
#       VALUES (1, 'Rohan', 14, 'Delhi', 200)");
# cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
#       VALUES (2, 'Allen', 14, 'Bangalore', 150 )");
# cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
#       VALUES (3, 'Martha', 15, 'Hyderabad', 200 )");
# cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
#       VALUES (4, 'Palak', 15, 'Kolkata', 650)");
#
# for row in cursor.execute("SELECT id, name, marks from SCHOOL"):
#     print("ID = ", row[0])
#     print("NAME = ", row[1])
#     print("MARKS = ", row[2], "\n")

print("Opened database successfully")