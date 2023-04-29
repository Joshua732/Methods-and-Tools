from Checkout import *
import OrderHistory
import Account
import Inventory

def home(userId):
  print("Welcome to the homescreen")

  #Creates an object of each class
  currentuser = OrderHistory.OrderHistory(userId)
  account = Account.Account(userId)
  inventory = Inventory.Inventory()

  while 1:
    print("1. User Account\n2. Shop\n3. Logout")
    x = int(input("Enter your choice: "))
    print("")

    match x:
      case 1:
        # User Account Screen options
        while 1:
          print("1. View your account info\n2. Edit your account info\n3. View Orderhistory\n4. Delete your account\n5. Go back")
          y = int(input("Enter your choice: "))

          match y:
            case 1:
              # View Account
              account.accInfo()

            case 2:
              # Edit Account info
              print("1. Edit your name\n2. Edit your date of birth\n3. Update your password")
              print("4. Edit your shipping address\n5. Edit your billing address\n6. Edit your payment info\n7. Go back")
              w = int(input("Enter your choice: "))

              match w:
                case 1:
                  # Edit account name
                  account.editname()
                  
                case 2:
                  # Edit date of birth
                  account.editdob()

                case 3:
                  # Edit password
                  account.editpass()

                case 4:
                  # Edit shipping info
                  account.editship()

                case 5:
                  # Edit billing address
                  account.editbill()

                case 6:
                  # Edit payment info
                  account.editpay()

                case 7:
                  # Go back
                  break

                case _:
                  # default case
                  print("Invalid choice... Try again!")

            case 3:
              # View orderhistory
              currentuser.viewOrderHistory()

            case 4:
              # Delete your account
              DeleteFromCartAccountDelete(userId)
              currentuser.deleteHistory()
              account.Accdel()
              return
            
            case 5:
              # Go back
              break

            case _:
              # Default case
              print("Invalid choice... Try again")
              
      case 2:
        # Cart Screen options
        while 1:
          print("1. View all items in a category\n2. View all items in cart")
          print("3. Add item to cart\n4. Remove items from cart")
          print("5. Checkout items\n6. Go back to home")
          y = int(input("Enter your choice: "))

          match y:
            case 1:
              # View inventory
              inventory.viewInventory()

            case 2:
              # View cart
              ViewCart(userId)

            case 3:
              # Add to cart
              AddToCart(userId)

            case 4:
              # Delete from cart
              DeleteFromCart(userId)

            case 5:
              # Checkout
              currentuser.addOrderToHistory()
              CheckoutFromCart(userId)
            case 6:
              # Go back
              break

            case _:
              # Default case
              print("Invalid choice... Try again!")

      case 3:
        # Logout
        print("Logging out...")
        break
        
      case _:
        # Default case
        print("Invalid choice... Try again!")


def main():
  print("Welcome!")
  while 1:
    print("1. Login\n2. Create an account\n3. Exit")
    a = int(input("Enter your choice: "))

    match a:
      case 1:
        # Login Screen
        userId = Account.login()
        if userId != False:
          home(userId)
        else:
          print("Invalid")

      case 2:
        # Create account screen
        
        userId = Account.createAccount()
        home(userId)

      case 3:
        # Exit program
        print("Goodbye!")
        break

      case _:
        # default case
        print("Invalid choice... Try again!")

main()
