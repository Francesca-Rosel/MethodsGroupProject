import sqlite3

#connecting to the database
db = sqlite3.connect("cartTable.db")
c = db.cursor()

#create database
class Cart:

    def __init__(self, databaseName="", tableName=""):
        self.databaseName = databaseName
        self.tableName = tableName

    def Cart(self, databaseName, tableName):
        self.databaseName = 'cartitems.db'
        self.tableName = 'cartTable'
    
    def viewCart(userID, inventoryDatabase):
        return None
        
    def addToCart(userID, ISBN):
        return None
    
    def removeFromCart(userID, ISBN):
        return None
    
    def checkOut(userID):
        return None
