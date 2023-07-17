# Connect To Database and Execute SQL Queries

insert_query = "insert into employeeinfo values(111,'Sourabh',7020529877,'Sangli','IT',90000,25000)"
update_query = "update employeeinfo set ename='Raj' where eid=111"
delete_query = "delete from employeeinfo where eid=111"

import cx_Oracle  # Install respective connector as per database
import os

try:
    os.environ["PATH"]="C:\\Testing\\PythonPractice\\oracle\\instantclient_21_8"
    con = cx_Oracle.connect("system", "system", "localhost/xe")
    curs = con.cursor()  # Create Cursor
    curs.execute(delete_query)  # Execute query through cursor
    curs.close()
    con.commit()
    con.close()
except:
    print("Connection Unsuccessful")

print("Finished......")