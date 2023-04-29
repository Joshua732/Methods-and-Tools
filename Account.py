import sqlite3
import sys
try:
    connection = sqlite3.connect("Workbase.db")

except:
    print("Connection does not work")
    sys.exit()
cursor = connection.cursor()

def login():
    userinput = input("What is your User ID? \n")
    cursor.execute(f"SELECT * FROM user WHERE UserID ={userinput}")
    userlist = cursor.fetchall()
    for x in userlist:
        passwordinput = input("What is your password? \n")
        if (passwordinput == x[3]):
            print("Logged in\n")
            return userinput
        else:
            print("Incorrect user ID or password\n")
            return False

def createAccount():
    try:
        connection = sqlite3.connect("Workbase.db")
    
    except:
        print("Connection does not work")
        sys.exit()
        
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM user WHERE UserID != -1")
    userlist = cursor.fetchall()
    i = 0
    for x in userlist:#increments i to make new unique id
        i+=1
    
    print("Welcome to account creation\n")
    
    fname = input("Please enter your first name\n")
    lname = input("Please enter your last name\n")
    password = input("Please enter password\n")
    bil = input("Please enter your billing address\n")
    ship = input("Please enter your shipping address\n")
    dob = input("Please enter your date of birth\n")
    cnum = input("Please enter your credit or debit card number\n")
    csv = input("Please enter your card security number\n")
    
    
    cursor.execute("INSERT INTO user (UserId, FirstName, LastName, Password, BillingAddress, ShippingAddress, DateOfBirth, CardNumber, SecurityNumber) VALUES(?,?,?,?,?,?,?,?,?)", (i, fname, lname,password,bil,ship,dob,cnum,csv))
    connection.commit()
    print("Account created\n")
    cursor.close()
    connection.close()
    return i #returns UserId        

class Account:
    def __init__(self, userID):
        self.userID = userID
    def __delete(self, userID):
        del self.userID
    
    def accInfo(self):
        cursor.execute(f"SELECT * FROM user WHERE UserId={self.userID}")
        userlist = cursor.fetchall()
        for x in userlist:
            print("User ID:", x[0])
            print("First name:", x[1])
            print("Last Name:", x[2])
            print("Password:", x[3])
            print("Billing Address:", x[4])
            print("Shipping Address:", x[5])
            print("Date of birth:", x[6])
            print("Card number:", x[7])
            print("Security code:", x[8])
            
        return True
    
    
    
    def Accdel(self):

        cursor.execute("DELETE FROM user WHERE UserId=?", (self.userID,))
        connection.commit()
        return True
        
    def editname(self):
        newfname = input("What is your updated first name? \n")
        newlname = input("What is your updated last name? \n")
        cursor.execute("UPDATE user SET FirstName=? WHERE UserId=?", (newfname, self.userID))
        cursor.execute("UPDATE user SET LastName=? WHERE UserId=?", (newlname, self.userID))
        connection.commit()
        return True
        
    def editdob(self):
        newdob = input("What is your updated date of birth \n")
        cursor.execute("UPDATE user SET DateOfBirth=? WHERE UserId=?", (newdob, self.userID))
        connection.commit()
        return True
    
    def editpass(self):
        newpass = input("What is your updated password \n")
        cursor.execute("UPDATE user SET Password=? WHERE UserId=?", (newpass, self.userID))
        connection.commit()
        return True
        
    def editship(self):
        newship = input("What is your new shipping address? \n")
        cursor.execute("UPDATE user SET ShippingAddress=? WHERE UserId=?", (newship, self.userID))
        connection.commit()
        return True
    
    def editbill(self):
        newship = input("What is your new billing address? \n")
        cursor.execute("UPDATE user SET BillingAddress=? WHERE UserId=?", (newship, self.userID))
        connection.commit()
        return True
        
    def editpay(self):
        newcnum = input("What is your new credit or debit card number? \n")
        newcsv = input("What is your new card's security number? \n")
        cursor.execute("UPDATE user SET CardNumber=? WHERE UserId=?", (newcnum, self.userID))
        cursor.execute("UPDATE user SET SecurityNumber=? WHERE UserId=?", (newcsv, self.userID))
        connection.commit()
        return True
        
