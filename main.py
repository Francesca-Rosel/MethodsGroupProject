import user
import inventory
import cart
#main function

def main(): 
  while True:
    print("Welcome to The Online Bookstore! \nPlease select a valid option. \n1.Login \n2.Create Account \n3.Exit") 
    option = input("Please choose a valid option: ")
    print('\n')

    match option:
      case '1':
        #Logged In Main Menu
        strawberry = user.user_class()
        strawberry.login()
        loggedIn = strawberry.getLoggedIn()
        while (loggedIn == True):
          print("1. View Account Information \n2. Inventory Information \n3. Cart Information\n4. Logout")
          option1 = input("Please choose a valid option: ")
          print('\n')
          match option1:
            #View Account Information: 
            case '1': 
              strawberry.viewAccountInformation()
            #View Inventory Information
            case '2': #connect to inventory class
              blackberry = inventory.inventory_class()
              print("1. View Inventory\n2. Search Inventory\n3. Go back")
              option2 = input("Choose a valid option: ")
              match option2:
                case '1':
                  blackberry.view_inventory()
                case '2': 
                  blackberry.search_inventory()
                case '3': #Go back
                  print("") #FIXME
                case _:
                  print("Invalid choice. Try Again.")
            #View Cart Information
            case '3': #connect to cart class
              blueberry = cart.cart_class()
              userID = strawberry.getUserID()
              print("1. View Cart\n2. Add Items to Cart\n3. Remove an Item from Cart\n4. Check Out\n5. Go back")
              option3 = input("Choose a valid option: ")
              match option3:
                case '1': 
                  inventoryDatabase = 'Inventory.db'
                  blueberry.viewCart(userID, inventoryDatabase)
                case '2': 
                  ISBN_add = input("Input ISBN of desired book: ")
                  blueberry.addToCart(userID, ISBN_add)
                case '3': 
                  ISBN_rem = input("Input ISBN of book to remove: ")
                  blueberry.removeFromCart(userID, ISBN_rem)
                case '4': 
                  blueberry.checkOut(userID)
                case '5': #Go back
                  print("") #FIXME
                case _:
                  print("Invalid choice. Try Again.")
            case '4':
              strawberry.logout()
              break
            case _:
              print("Invalid option. Choose again.") 
        #Failed Log In Attempt fails to enter while loop and leads back to main menu.
      case '2':
        strawberry.createAccount()
      case '3':
        print("Thank you for shopping with us! Good-bye") 
        return False
      case _:
        print("Invalid option. Choose again.")
  

#this is calling the main function
main()
