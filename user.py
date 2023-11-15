# user class. Tommy
import sqlite3

# connect to the database
db = sqlite3.connect('users.db')

# create a cursor object
c = db.cursor()

# create a table
c.execute('''CREATE TABLE userTable (UserID TEXT PRIMARY KEY NOT NULL, Email TEXT NOT NULL, Password TEXT NOT NULL, FirstName TEXT NOT NULL, LastName TEXT NOT NULL, Address TEXT NOT NULL, City TEXT NOT NULL, State TEXT NOT NULL, Zip INT NOT NULL, Payment TEXT NOT NULL)''')

#populating with some random values from online generators
#random values: FirstName, LastName, Address, City, State, Zip
            #FirstName, LastName came from an online generator. Possible these are real people somewhere in the world
            #Address, City, Zip are random values from an online generator given a random state. Possible these are real addresses
c.execute('''INSERT INTO userTable (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES ('wf123', 'wfreeman1@gmail.com', 'HailState98!', 'Willie', 'Freeman', '2970 Froe St.', 'Paden City', 'West Virginia', '26159', 'PayPal')''')
c.execute('''INSERT INTO userTable (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES ('fg456', 'fgarret2@gmail.com', 'MikeLeach23!', 'Freyja', 'Garret', '4567 Archwood Ave.', 'Newcastle', 'Wyoming', '82701', 'Visa')''')
db.commit()

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
    num = 0
              
    attemptUser = input("Enter UserID: ")
    attemptPassword = input("Enter Password: ")

    c.execute('''SELECT UserID, Password FROM userTable''')

    loginInfo = c.fetchall()
    for id in loginInfo:
        if ((attemptUser == loginInfo[num][0]) and (attemptPassword == loginInfo[num][1])):
            self.userID = attemptUser
            print("Logged In Successfully\n")
            self.loggedIn = True
            return True
        num += 1
    print("Login Failed. Check your UserID and Password! Try Again. \n")
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
