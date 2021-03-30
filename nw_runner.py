# Establish a connection to a SQL DB using pyodbc
import pyodbc
from nw_products import NwProducts

# Define important connection variables
ip = "XXX"
database = "XXX"
uname = "XXX"
passwd = "XXX"

# Define the connection settings
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' +
                            f'SERVER={ip};DATABASE={database};UID={uname};PWD={passwd}')


if __name__ == "__main__":
    stock = NwProducts("Products", connection)
    print(stock.count_stock("Chai"))
    stock.update_stock("Chai", 14)


    del stock;





