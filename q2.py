
import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='oasis3005', host='localhost', database='tabelsq2')

# Create a cursor
cursor = cnx.cursor()
# Create new table
cursor.execute("CREATE TABLE output1 (name VARCHAR(255), count INT)")


# Insert data into the new table
cursor.execute("INSERT INTO output1 (name,count) SELECT department.NAME, COUNT(employee.ID) FROM employee JOIN department WHERE employee.DEPT_ID= department.ID GROUP BY department.NAME ORDER BY COUNT(employee.ID) DESC, department.NAME ASC")

# Insert department that not inside the Employee table, and not already  in the new table
cursor.execute("INSERT INTO output1 (name,count) SELECT department.NAME, 0 FROM department WHERE department.name NOT IN (SELECT department.ID FROM employee) AND department.name NOT IN (SELECT name FROM output1) ORDER BY department.NAME ASC")
# Commit the changes
cnx.commit()

# Close the cursor and connection
cursor.close()
cnx.close()