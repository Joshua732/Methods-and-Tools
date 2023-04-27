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
cursor.execute("SELECT * FROM Inventory")
print(cursor.fetchall())

class Inventory:

    # displays menu
    def menuDisplay(self):
        print("-----Inventory-----")
        print("1. Display Inventory")
        print("2. Update Inventory")
        print("3. Add item")
        print("4. Remove item")
        print("5. Exit")
        option = int(input("Select an option: "))

    # function for viewing inventory
    def viewInventory(self):
        cursor.execute("SELECT * FROM Inventory")
        display = cursor.fetchall()

        for i in display:
            print("Item Name: ", i[0])
            print("Item Description: ", i[1])
            print("Item Number: ", i[2])
            print("Item Quantity: ", i[3])
            print("Item Cost: ", i[4])
            print("Item Availability: ", i[5])
            print("\n")

    # function that updates inventory based on input
    def updateInventory(self):
        quantitySub = int(input("Enter quantity to be updated: "))
        itemNum = input("Select itemID to be updated: ")
        cursor.execute("UPDATE Inventory SET itemQuantity = itemQuantity - ? WHERE itemNum = ?", (quantitySub, itemNum))
        connection.commit()

        # updates item availability when quantity 0
        cursor.execute("SELECT itemQuantity FROM Inventory WHERE itemNum=?", (itemNum,))
        oos = cursor.fetchone()[0]
        if oos == 0:
            availUpdate = "out of stock"
            cursor.execute(("UPDATE Inventory SET itemAvailability =? WHERE itemNum=?"), (availUpdate, itemNum))
            connection.commit()

        print("\nInventory Updated\n")
        cursor.execute("SELECT * FROM Inventory WHERE itemNum= ?", (itemNum,))

    # adds items to database
    def itemAdd(self):
        name = input("Enter item name: ")
        desc = input("Enter item description: ")
        itemID = input("Enter item ID: ")
        quantity = input(":Enter quantity: ")
        cost = input("Enter cost: ")
        availability = input("Enter availability: ")
        cursor.execute("INSERT INTO Inventory VALUES (?,?,?,?,?,?)", (name, desc, itemID, quantity, cost, availability))
        connection.commit()
        print("item added\n")

    # removes items from database
    def itemRemove(self):
        itemRemove = int(input("Enter item ID to be deleted: "))
        cursor.execute("DELETE FROM Inventory WHERE itemNum= ?", (itemRemove,))
        connection.commit()
        print("Item deleted\n")











    