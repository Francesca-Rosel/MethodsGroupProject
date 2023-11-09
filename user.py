# user class. Tommy
class user_class:
  databaseName = ""
  tableName = ""
  userID = ""
  loggedIn = False
  def __init__(self, databaseName, tableName, userID, loggedIn):
    self.databaseName = databaseName
    self.tableName = tableName
    self.userID = userID
    self.loggedIn = loggedIn
  def User(self, databaseName, tableName):
    self.databaseName = databaseName
    self. tableName = tableName
user = user_class()
