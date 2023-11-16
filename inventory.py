# inventory class - Amelia
import sqlite3

db = sqlite3.connect("inventory.db")
c = db.cursor()
#create database
c.execute(''' CREATE TABLE "inventory.db" (
	"ISBN"	TEXT NOT NULL,
	"Title"	TEXT NOT NULL,
	"Author" TEXT NOT NULL,
	"Genre"	TEXT NOT NULL,
	"Pages"	TEXT NOT NULL,
	"releaseData"	TEXT NOT NULL,
	"Stock"	TEXT NOT NULL,
	PRIMARY KEY("ISBN")
);''')

class Inventory:
    # initializes
    def _init_(self, database="", table=""):
        self.database = database
        self.table = table

    def Inventory(self, database, table):
        self.database=database
        self.table=table

    # view inventory
    def view_inventory(self):
        print("Inventory: \n")
        print("---------")
        c.execute("SELECT * FROM inventory")

        rows = c.fetchall()
        num = 1;
        for row in rows:
            print("Book " + num + ":\n")
            print(row[0] + " | " + row[1] + " | " + row[2] + " | " + row[3] + " | " + row[4] + " | " + row[5] + " | " + row[6] + "\n")
            num+=1

    # search inventory
    def search_inventory(self):
        item = input("Enter the title of the item you'd like to find\n")
        c.execute(("SELECT * FROM inventory WHERE Title=?", (item,)))
        #finish this later

    # decrease stock
    def decrease_stock(self, isbn=""):
        self.isbn=isbn
        print()

    # GETTERS
    def get_db_name(self):
        return self.database
        
    def get_table_name(self):
        return self.table
