# Connect to Databases and Execute SQL queries
select_query = "select * from employeeinfo"

import cx_Oracle  # Install respective connector as per database
import os

try:
    os.environ["PATH"]="E:\\Testing\\PythonPractice\\oracle\\instantclient_21_8"
    con = cx_Oracle.connect("system", "system", "localhost/xe")
    curs = con.cursor()  # Create Cursor
    curs.execute(select_query)  # Execute query through cursor
    # print(curs)  #MySqlCursor: select * from student  // we can not print cursor value

    for row in curs:
        print(row[0], row[1])  # To access table row data  // It will print all the data drom db table
        #So we can use this data for automation test data

    curs.close()
    con.close()
except:
    print("Connection Unsuccessful")

print("Finished......")