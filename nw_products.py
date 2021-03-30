import pyodbc


# backup_Products is a backup of Products I made
# This class is for the stock department
class NwProducts:

    def __init__(self, table_name, connection):
        self.table_name = "branson_" + table_name
        self.database = connection
        self.cursor = connection.cursor()
        self.__gen_table(table_name)

    def __del__(self):
        self.database.close()

    # This is because I don't actually want to use the real table
    def __gen_table(self, table_name):
        try:  # Try and print the contents of the table
            print(self.__fetch_rows(f"SELECT * FROM {self.table_name};"))
        except pyodbc.ProgrammingError:  # If it doesnt exist then clone the original
            self.cursor.execute(f"SELECT * INTO {self.table_name} FROM {table_name};")
        finally:  # Try and print it again
            print(self.__fetch_rows(f"SELECT * FROM {self.table_name};"))

    def __fetch_rows(self, query):
        return self.cursor.execute(query).fetchall()

    def __fetch_single(self, query):
        return self.cursor.execute(query).fetchone()

    def count_stock(self, product):
        row = self.__fetch_single(f"SELECT UnitsInStock FROM {self.table_name} WHERE ProductName = '{product}';")
        return row[0]

    def update_stock(self, product, count):
        self.cursor.execute(f"UPDATE {self.table_name} SET UnitsInStock={count} WHERE ProductName = '{product}';")

    def subtract_stock(self, product, count):
        pass

    def add_stock(self, product, count):
        pass
