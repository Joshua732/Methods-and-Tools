import sqlite3
import sys

# connecting to the database
try:
    connection = sqlite3.connect("Workbase.db")

    print("Database connected")


# terminates the program if connection is unsuccessful
except:
    print("Database failed to connect")

    sys.exit()

# space
print()

# allows queries to be sent
cursor = connection.cursor()

class Inventory:

    # displays menu
    # not needed for project but left in
    def menuDisplay(self):
        print("-----Inventory-----")
        print("1. Display Inventory")
        print("2. Update Inventory")
        print("3. Add item")
        print("4. Remove item")
        print("5. Exit")

    # function for viewing inventory
    def viewInventory(self):
        cursor.execute("SELECT * FROM inventory")
        display = cursor.fetchall()

        # loop displays items
        for i in display:
            print("Item Num: ", i[0])
            print("Item Name: ", i[1])
            print("Item Description: ", i[2])
            print("Item Quantity: ", i[3])
            print("Item Cost: ", i[4])
            print("\n")

    # function that updates inventory based on input
    def updateInventory(self, quantitySub, itemName):

        # updates the database
        cursor.execute("UPDATE inventory SET itemQuantity = itemQuantity - ? WHERE itemName = ?", (quantitySub, itemName))
        connection.commit()
        
        cursor.execute("SELECT * FROM inventory WHERE itemId= ?", (itemName,))

    # adds items to database
    # not needed for project but left in
    def itemAdd(self):
        name = input("Enter item name: ")
        desc = input("Enter item description: ")
        itemID = input("Enter item ID: ")
        quantity = input(":Enter quantity: ")
        cost = input("Enter cost: ")
        cursor.execute("INSERT INTO inventory VALUES (?,?,?,?,?)", (itemID, name, desc, quantity, cost))
        connection.commit()
        print("item added\n")

    # removes items from database
    # not needed for project but left in
    def itemRemove(self):
        itemRemove = int(input("Enter item ID to be deleted: "))
        cursor.execute("DELETE FROM inventory WHERE itemId= ?", (itemRemove,))
        connection.commit()
        print("Item deleted\n")

