#Cart Class - Francesca

import sqlite3
import inventory 

#connecting to the database
db = sqlite3.connect("cartitems.db")
c = db.cursor()

#create database
c.execute('''CREATE TABLE IF NOT EXISTS cartTable (UserID TEXT NOT NULL, ISBN TEXT NOT NULL, Quantity TEXT NOT NULL, FOREIGN KEY (UserID) REFERENCES userTable(UserID), FOREIGN KEY (ISBN) REFERENCES inventoryTable(ISBN))''')

db.commit()

class cart_class:

    def _init_(self, databaseName="", tableName=""):
        self.databaseName = databaseName
        self.tableName = tableName

    def Cart(self, databaseName, tableName):
        self.databaseName = 'cartitems.db'
        self.tableName = 'cartTable'
    
    def viewCart(self, userID, inventoryDatabase):
        
        #conn = sqlite3.connect("Inventory.db", "cartitems.db")
        #c = conn.cursor()
        #except:
            #conn.exit()
        conn_main = sqlite3.connect('Inventory.db')
        c_main = conn_main.cursor()

        #I tried so hard trying to figure this out please have mercy on me. 

        print("Shopping Cart:\n")
        #c.execute("SELECT * FROM inventoryTable INNER JOIN cartTable ON inventoryTable.ISBN = cartTable.ISBN AND UserID =?", (userID,))
        c_main.execute("""SELECT * FROM inventoryTable INNER JOIN cartitems.cartTable ON inventoryTable.ISBN = cartitems.cartTable.ISBN AND cartitems.cartTable.UserID =?""", (userID,))
        db.commit()

        #rows = c.fetchall()
        rows = c_main.fetchall()
        num = 1
        for row in rows:
            print("----------\n")
            print("Book " + str(num) + ":\n")
            print(row[0] + " | " + row[1] + " | " + row[2] + " | " + row[3] + " | " + row[4] + " | " + row[5] + " | " + row[6] + "\n")
            num+=1
        
        
    def addToCart(self, userID, ISBN):
        desiredQuantity = input("Number of copies: ")
        c.execute("INSERT INTO cartTable VALUES(?, ?, ?)", (userID, ISBN, desiredQuantity))
        db.commit()
      
    
    def removeFromCart(self, userID, ISBN):
        c.execute("DELETE FROM cartTable WHERE UserID =? AND ISBN =?", (userID, ISBN))
        db.commit()
        return None
    
    def checkOut(self, userID):
        blackberry = inventory.inventory_class()
        c.execute("SELECT * FROM cartTable WHERE UserID =?", (userID,))
        cartInfo = c.fetchall()
        num = 0
        for i in range(cartInfo[num][2]):
            blackberry.decrease_stock(cartInfo[num][1])
            num += 1
        c.execute("DELETE FROM cartTable WHERE UserID =?", (userID,))
        db.commit()

        
