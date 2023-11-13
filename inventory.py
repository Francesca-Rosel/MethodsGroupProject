# inventory class
import sqlite3

db = sqlite3.connect("inventory.db")
c = db.cursor()
#finish and test database commands
c.execute(''' CREATE TABLE inventoryTable ()''')

class Inventory:
    # initializes
    def _init_(self, database="", table=""):
        self.database = database
        self.table = table

    def Inventory(self, database, table):
        self.database=database
        self.table=table

    # getter - db name
    def get_db_name(self):
        return self.database

    # getter - table name
    def get_table_name(self):
        return self.table

    # view inventory
    def view_inventory(self, db_list):
        for x in db_list:
            print(x)

    # search inventory
    def search_inventory(self, item):
        self.db_name = item
        print()

    # decrease stock
    def decrease_stock(self, isbn):
        self.isbn=isbn
        print()
