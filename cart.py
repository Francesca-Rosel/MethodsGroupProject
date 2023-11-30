#Cart Class - Francesca

import sqlite3
import inventory

#connecting to the database
db = sqlite3.connect("cartTable.db")
c = db.cursor()

#create database
#create database
c.execute(''' CREATE TABLE IF NOT EXISTS cartTable (
	FOREIGN KEY(UserID) REFERENCES userTable(UserID),
    FOREIGN KEY(ISBN) REFERENCES inventoryTable(ISBN),
    "Quantity" TEXT NOT NULL    
	
); ''')


class Cart:
    

    def __init__(self, databaseName="", tableName=""):
        self.databaseName = databaseName
        self.tableName = tableName

    def Cart(self, databaseName, tableName):
        self.databaseName = 'cartitems.db'
        self.tableName = 'cartTable'
    
    def viewCart(userID, inventoryTable):
        print("Shopping Cart:\n")
        c.execute("SELECT * FROM inventoryTable INNER JOIN cartTable ON inventoryTable.ISBN = cartTable.ISBN AND UserID =?", (userID,))

        rows = c.fetchall()
        num = 1
        for row in rows:
            print("----------\n")
            print("Book " + str(num) + ":\n")
            print(row[0] + " | " + row[1] + " | " + row[2] + " | " + row[3] + " | " + row[4] + " | " + row[5] + " | " + row[6] + "\n")
            num+=1
        return None
        
    def addToCart(userID, ISBN):
        attemptedISBN = input("Input ISBN of desired book: ")
        desiredQuantity = input("Number of copies: ")
        '''c.execute("SELECT Stock FROM inventoryTable WHERE ISBN =?", (attemptedISBN,))
        available = c.fetchone()
        while (desiredQuantity > int(available[0])):
            print("Error. Not Enough Stock. Please choose less than ", available)
            desiredQuantity = input("Number of copies: ")
        '''
        c.execute("INSERT INTO cartTable (UserID, ISBN, Quantity)")
        c.execute()
        return None
    
    def removeFromCart(userID, ISBN):
        return None
    
    def checkOut(userID):
        blackberry = inventory.inventory_class()
        c.execute("SELECT * FROM cartTable WHERE UserID =?", (userID,))
        cartInfo = c.fetchall()
        num = 0
        for i in range(cartInfo[num][2]):
            blackberry.decrease_stock(cartInfo[num][1])
            num += 1
        
        return None
