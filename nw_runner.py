# Establish a connection to a SQL DB using pyodbc
import pyodbc
from nw_products import NwProducts

# Define important connection variables
ip = "18.135.103.95"
database = "Northwind"
uname = "SA"
passwd = "Passw0rd2018"

# Define the connection settings
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' +
                            f'SERVER={ip};DATABASE={database};UID={uname};PWD={passwd}')


if __name__ == "__main__":
    stock = NwProducts("Products", connection)
    stock.count_stock("Chai")
    print(stock.count_stock("Aniseed Syrup"))





