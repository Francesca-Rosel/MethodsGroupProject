# inventory class - Amelia
import sqlite3

db = sqlite3.connect("inventoryTable.db")
c = db.cursor()
#create database
c.execute(''' CREATE TABLE "inventoryTable" (
	"ISBN"	TEXT NOT NULL,
	"Title"	TEXT NOT NULL,
	"Author" TEXT NOT NULL,
	"Genre"	TEXT NOT NULL,
	"Pages"	TEXT NOT NULL,
	"ReleaseDate" TEXT NOT NULL,
	"Stock"	TEXT NOT NULL,
	PRIMARY KEY("ISBN")
); ''')

#add data
c.execute('''INSERT INTO inventoryTable (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) VALUES ('9781250891211', 'A Darker Shade of Magic', 'V.E Schwab', 'Fantasy', '416', '05/16/2023', '25')''')
c.execute('''INSERT INTO inventoryTable (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) VALUES ('9780062484390', 'And Then There Were None', 'Agatha Christie', 'Mystery', '256', '11/06/1939', '7') ''')
c.execute('''INSERT INTO inventoryTable (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) VALUES ('9780811204811', 'No Longer Human', 'Osamu Dazai', 'Fiction', '176', '01/17/1973', '15') ''')
c.execute('''INSERT INTO inventoryTable (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) VALUES ('9781716675522', 'Data Structures and Advanced Algorithms: Python', 'Rachel Xin Tony Lee Elisabeth Feng', 'Non-Fiction', '192', '08/07/2020', '5') ''')
c.execute('''INSERT INTO inventoryTable (ISBN, Title, Author, Genre, Pages, ReleaseDate, Stock) VALUES ('9780141196886', 'Dracula', 'Bram Stoker', 'Horror', '512', '05/26/1897', '5') ''')
db.commit()

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
        c.execute("SELECT * FROM inventoryTable")

        rows = c.fetchall()
        num = 1;
        for row in rows:
	    print("---------\n")
            print("Book " + num + ":\n")
            print(row[0] + " | " + row[1] + " | " + row[2] + " | " + row[3] + " | " + row[4] + " | " + row[5] + " | " + row[6] + "\n")
            num+=1

    # search inventory
    def search_inventory(self):
        item = input("Enter the title of the item you'd like to find: ")
        c.execute(("SELECT * FROM inventoryTable WHERE Title=?", (item,)))
        result = c.fetchone();

	#checks if exists
        if result:
            self.view_inventory()
        else:
            print("\n Search failed. Please enter a valid title. \n")

    # decrease stock
    def decrease_stock(self, isbn=""):
        self.isbn=isbn
        currStock = c.execute(("SELECT Stock FROM inventoryTable WHERE ISBN=?",(isbn,)))
        currStock-=1
	    
        #update with new stock value
        c.execute(("UPDATE inventoryTable SET Stock=? WHERE ISBN=?",(currStock, isbn,)))
	db.commit()

    # GETTERS
    def get_db_name(self):
        return self.database
        
    def get_table_name(self):
        return self.table
