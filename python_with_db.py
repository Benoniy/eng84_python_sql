# Establish a connection to a SQL DB using pyodbc
import pyodbc

# Define important connection variables
ip = "18.135.103.95"
database = "Northwind"
uname = "SA"
passwd = "Passw0rd2018"

# Define the connection settings
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' +
                            f'SERVER={ip};DATABASE={database};UID={uname};PWD={passwd}')


# Creation of our controller (cursor)
cursor = connection.cursor()


# Fetch data from northwind
print(cursor.execute("SELECT @@version;"))  # Execute a search query
row = cursor.fetchone()  # Fetch the first row of the result directly from the cursor
print(row)  # Print the result


# Fetch data from a table
cust_rows = cursor.execute("SELECT * FROM CUSTOMERS").fetchall()
print(cust_rows)


# Iterate through results
prod_rows = cursor.execute("SELECT * FROM PRODUCTS").fetchall()

# Go through each row in a collection of results
for row in prod_rows:
    print(row.UnitPrice)  # Columns become instance variables of rows


connection.close()
