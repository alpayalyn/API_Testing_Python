import mysql.connector
# OUR GOAL HERE IS TO MANIPULATE THE SQL TABLE/CONTENTS NOT ON DIFFERENT PROGRAMME BUT BY PYTHON HERE !!!
# host, database, user, password
# below we are connecting to the mysql server.
# conn = mysql.connector.connect(host='localhost',database='PythonAutomation',user='root',password='rahulshettyacademy')
# below checking we are connected or not.
print(conn.is_connected())

# below we defined a Cursor we go through the table located in the DB server.
cursor = conn.cursor()
# Cursor brings selected the whole table which is named as CustomerInfo
cursor.execute('select * from CustomerInfo')

# fetchone function will only fetch the row where the cursor is pointed at.
# also rows are type of TUPLE!!! its similar to LIST you can reach to them by [ ... ] entering some number.
# row = cursor.fetchone()

rows = cursor.fetchall()
print(rows)
sum = 0
for row in rows:
    sum = sum + row[2]

print(sum)
# we can close by the function below.

# In the query there shouldn't be any valaue assigned to the variable. %s means there will be string.
query = "update customerInfo set Location = %s where CourseName = %s"
data = ("UK","Jmeter")
# Python intellegence is enough to put the DATA TUPLE into QUERY thanks to %s.
cursor.execute(query,data)
conn.commit()


conn.close()


