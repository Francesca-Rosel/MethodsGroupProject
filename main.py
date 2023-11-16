#from user import *
#from inventory import *
#main function
def logIn():
  while True:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    login = True
    #if username and password in database then set to true. if not set login to false.
    if (login == True):
        return False 
    #Direct user to logged in menu
    elif(login == False):
        print("incorrect username or password. Please try again.")
        #back to menu
        return False  

      
def main():
  #outermenu = True
  #innermenu = False
  while True:
    print("Welcome to The Online Bookstore! \nPlease select a valid option. \n1.Login \n2.Create Account \n3.Logout") 
    option = input("Please choose a valid option: ")

    match option:
      case '1':
        print("login section")
        logIn()
        return False
      case '2':
        print("create account section")
        return False
      case '3':
        print("Thank you for shopping with us! Good-bye")
        return False
  

#this is calling the main function
main()
