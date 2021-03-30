# Python with sql
## PYODBC:
### Potential solution for debugging driver issues:  
This will not work unless you have the connection driver you want to use installed.  
So I have provided a [link to the driver](https://docs.microsoft.com/en-gb/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15) I needed for this connection



### Establish a connection with PYODBC:
```python
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
```
### Fetch data from a database:  
1. Fetch a single row.
```python
# Fetch data from northwind
print(cursor.execute("SELECT @@version;"))  # Execute a search query
row = cursor.fetchone()  # Fetch the first row of the result directly from the cursor
print(row)  # Print the result
```
2. Fetch all the rows for a query.
```python
# Fetch data from a table
cust_rows = cursor.execute("SELECT * FROM CUSTOMERS").fetchall()
print(cust_rows)
```
3. Iterate through a fetch all.
```python
# Iterate through results
prod_rows = cursor.execute("SELECT * FROM PRODUCTS").fetchall()

# Go through each row in a collection of results
for row in prod_rows:
    print(row.UnitPrice)  # Columns become instance variables of rows
```

## Task - SQL OOP:
create an example of how we can create service objects related to a particular table.

## An sql manager for the products table

create an object that relates only to the products table in the Northwind database. The reason for creating a single  
object for any table within the database would be to ensure that all functionality we build into this relates to what  
could be defined as a 'business function'.  

As an example the products table, although relating to the rest of the company, will service a particular area of the  
business in this scenario we will simply call them the 'stock' department.  

The stock department may have numerous requirements and it makes sense to contain all the requirements a code actions  
within a single object. 

Create two files `nw_products.py` & `nw_runner.py` and then we will move into creating our object.  

APPLY OOP - DRY CRUD WHERE POSSIBLE   

### Solution:  

