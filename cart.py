#Cart Class - Francesca

import sqlite3
import inventory

#connecting to the database
db = sqlite3.connect("cartTable.db")
c = db.cursor()

#create database
c.execute('''CREATE TABLE IF NOT EXISTS userTable (UserID TEXT NOT NULL, ISBN TEXT NOT NULL, Quantity TEXT NOT NULL, FOREIGN KEY (UserID) REFERENCES userTable(UserID), FOREIGN KEY (ISBN) REFERENCES inventoryTable(ISBN))''')

db.commit()

class cart_class:

    def _init_(self, databaseName="", tableName=""):
        self.databaseName = databaseName
        self.tableName = tableName

    def Cart(self, databaseName, tableName):
        self.databaseName = 'cartitems.db'
        self.tableName = 'cartTable'
    
    def viewCart(self, userID, inventoryTable):
        print("Shopping Cart:\n")
        c.execute("SELECT * FROM inventoryTable INNER JOIN cartTable ON inventoryTable.ISBN = cartTable.ISBN AND UserID =?", (userID,))

        rows = c.fetchall()
        num = 1
        for row in rows:
            print("----------\n")
            print("Book " + str(num) + ":\n")
            print(row[0] + " | " + row[1] + " | " + row[2] + " | " + row[3] + " | " + row[4] + " | " + row[5] + " | " + row[6] + "\n")
            num+=1
        
        
    def addToCart(self, userID, ISBN):

        desiredQuantity = input("Number of copies: ")
        '''c.execute("SELECT Stock FROM inventoryTable WHERE ISBN =?", (attemptedISBN,))
        available = c.fetchone()
        while (desiredQuantity > int(available[0])):
            print("Error. Not Enough Stock. Please choose less than ", available)
            desiredQuantity = input("Number of copies: ")
        '''
        c.execute("INSERT INTO cartTable VALUES(?, ?, ?)", (userID, ISBN, desiredQuantity))
        
        
    
    def removeFromCart(self, userID, ISBN):
        return None
    
    def checkOut(self, userID):
        blackberry = inventory.inventory_class()
        c.execute("SELECT * FROM cartTable WHERE UserID =?", (userID,))
        cartInfo = c.fetchall()
        num = 0
        for i in range(cartInfo[num][2]):
            blackberry.decrease_stock(cartInfo[num][1])
            num += 1
        c.execute("TRUNCATE TABLE cartTable")

        
