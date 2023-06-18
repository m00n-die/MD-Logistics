"""Defines an item class that contains all attributes of items in an inventory"""

import sqlite3



conn = sqlite3.connect("mdl.db")
cur = conn.cursor()

class Item():
    """Defines the Item class"""
    def __inti__(self, itemName, price, quantity):
        """Initializes the class with itemName, price and quantity"""
        self.itemName = itemName
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        """Prints out the class in a nice way"""
        return "Item Name: {}\nPrice: {}\nQuantity: {}".format(self.itemName, self.price, self.quantity)
    
    def addItem():
        """Adds an item to the inventory table"""
        itemName = input("Enter name of item: ")
        confirmName = input("Re-enter name: ")
        if confirmName == itemName:
            price = input("Enter price of {}: ".format(itemName))
            qty = input("Quantity of {}: ".format(itemName))
            cur.execute("INSERT INTO inventory VALUES (NULL, ?, ?, ?)", (itemName, price, qty))
            conn.commit()
            print("Item added successfully")
        else:
            print("Name mismatch please check and try again.")

    def deleteItem():
        """Deletes an item from the inventory"""
        itemName = input("Enter name of item to be deleted: ")
        cur.execute("SELECT itemName from inventory WHERE itemName=?", (itemName,))
        exists = cur.fetchone()
        if exists:
            print("This action cannot be done")
            choice = input(f"Delete item: '{itemName}'. Y/N: ")
            if choice == 'Y':
                cur.execute("DELETE FROM inventory WHERE itemName=?", (itemName,))
            else:
                print("Action borted")
                exit()
        else:
            print("Item does not exist")