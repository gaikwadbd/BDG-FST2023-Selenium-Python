
# Create the connection object
import mysql as mysql

myconn = mysql.connector.connect(host="localhost:3308", user="root", passwd="root", database="sys")

# creating the cursor object
cur = myconn.cursor()

try:
    # Reading the Employee data
    cur.execute("select * from personal")

    # fetching the rows from the cursor object
    result = cur.fetchall()
    # printing the result

    for x in result:
        print(x);
except:
    myconn.rollback()

myconn.close()