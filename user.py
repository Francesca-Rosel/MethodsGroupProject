# user class. Tommy
import sqlite3

# connect to the database
conn = sqlite3.connect('users.db')

# create a cursor object
c = conn.cursor()

# create a table
c.execute('''CREATE TABLE userTable (UserID INT PRIMARY KEY NOT NULL, Email TEXT NOT NULL,
            Password TEXT NOT NULL, FirstName TEXT NOT NULL, LastName TEXT NOT NULL,
            Address TEXT NOT NULL, City TEXT NOT NULL, State TEXT NOT NULL, Zip INT NOT NULL,
            Payment TEXT NOT NULL)''')

class user_class:

  def __init__(self, databaseName = "", tableName = "", userID = "", loggedIn = False):
    self.databaseName = databaseName
    self.tableName = tableName
    self.userID = userID
    self.loggedIn = loggedIn

  def User(self, databaseName, tableName):
    self.databaseName = databaseName
    self.tableName = tableName

  def login(self):
    return False

  def logout(self):
      return False

  def viewAccountInformation(self):
      print()

  def createAccount(self):
      print()

  def getLoggedIn(self):
      return self.loggedIn

  def getUserID(self):
      return self.userID
