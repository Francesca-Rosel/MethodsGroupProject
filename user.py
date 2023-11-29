# user class. Tommy
import sqlite3

# connect to the database
db = sqlite3.connect('users.db')

# create a cursor object
c = db.cursor()

# create a table
c.execute('''CREATE TABLE IF NOT EXISTS userTable (UserID TEXT PRIMARY KEY NOT NULL, Email TEXT NOT NULL, Password TEXT NOT NULL, FirstName TEXT NOT NULL, LastName TEXT NOT NULL, Address TEXT NOT NULL, City TEXT NOT NULL, State TEXT NOT NULL, Zip INT NOT NULL, Payment TEXT NOT NULL)''')
#db.commit()

try:
    c.execute('''INSERT INTO userTable (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES ('wf123', 'wfreeman1@gmail.com', 'HailState98!', 'Willie', 'Freeman', '2970 Froe St.', 'Paden City', 'West Virginia', '26159', 'PayPal')''')
    c.execute('''INSERT INTO userTable (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES ('fg456', 'fgarret2@gmail.com', 'MikeLeach23!', 'Freyja', 'Garret', '4567 Archwood Ave.', 'Newcastle', 'Wyoming', '82701', 'Visa')''')
    db.commit()
except sqlite3.IntegrityError:
    print("")

#c.close()

# populating with some random values from online generators
    # random values: FirstName, LastName, Address, City, State, Zip
    # FirstName, LastName came from an online generator. Possible these are real people somewhere in the world
    # Address, City, Zip are random values from an online generator given a random state. Possible these are real addresses
#c.execute('''INSERT INTO userTable (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES ('wf123', 'wfreeman1@gmail.com', 'HailState98!', 'Willie', 'Freeman', '2970 Froe St.', 'Paden City', 'West Virginia', '26159', 'PayPal')''')
#c.execute('''INSERT INTO userTable (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES ('fg456', 'fgarret2@gmail.com', 'MikeLeach23!', 'Freyja', 'Garret', '4567 Archwood Ave.', 'Newcastle', 'Wyoming', '82701', 'Visa')''')

class user_class:

    def __init__(self, databaseName="", tableName="", userID="", loggedIn=False):
        self.databaseName = databaseName
        self.tableName = tableName
        self.userID = userID
        self.loggedIn = loggedIn

    def User(self, databaseName, tableName):
        self.databaseName = 'users.db'
        self.tableName = 'userTable'

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
        self.userID = ""
        self.loggedIn = False
        return False

    def viewAccountInformation(self):
        if (self.userID != ""):
            c.execute('''SELECT * FROM userTable''')
            accountInfo = c.fetchall()

            num = 0
            for info in accountInfo:
                if(self.userID == accountInfo[num][0]):
                    print("UserID: ", accountInfo[num][0])
                    print("Email: ", accountInfo[num][1])
                    print("Password: ", accountInfo[num][2])
                    print("First Name: ", accountInfo[num][3])
                    print("Last Name: ", accountInfo[num][4])
                    print("Address: ", accountInfo[num][5])
                    print("City: ", accountInfo[num][6])
                    print("State: ", accountInfo[num][7])
                    print("Zip: ", accountInfo[num][8])
                    print("Payment: ", accountInfo[num][9], "\n")
                    break

                num += 1

    def createAccount(self):
        print("Thank you for joining! Let's get started with some basic information about you.")

        newId = input("Enter a UserID: ")
        newEmail = input("Enter a valid email: ")
        newPassword = input("Enter a password: ")
        newFirst = input("Enter your first name: ")
        newLast = input("Enter your last name: ")
        newAdd = input("Enter your street address: ")
        newCity = input("Enter your city: ")
        newState = input("Enter your state: ")
        newZip = input("Enter your zip code: ")
        newPay = input("Enter your payment type: ")

        query = 'INSERT INTO userTable (UserID, Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) VALUES '
        query += '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' % (newId, newEmail, newPassword, newFirst, newLast, newAdd, newCity, newState, newZip, newPay)

        c.execute(query)
        db.commit()

    def getLoggedIn(self):
        return self.loggedIn

    def getUserID(self):
        return self.userID
