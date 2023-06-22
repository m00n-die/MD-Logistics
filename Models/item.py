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

    def update(id, price=None, quantity=None):
        """Function that takes optional input and then updates the itemName column
        with the arguments provided"""
        if price:
            cur.execute('UPDATE inventory SET price=? WHERE id=?', (price, id))
        if quantity:
            cur.execute('UPDATE inventory SET quantity=? WHERE id=?', (quantity, id))
        conn.commit()


    def updateItem():
        """Updates the data on an item"""
        itemName = input('Enter name of the item to be updated: ')
        cur.execute('SELECT itemName from inventory WHERE itemName=?', (itemName,))
        exists =cur.fetchone()
        if exists:
            Item.update()
        else:
            print('Item does not exist. Please check the name and try again!')
            exit()

    def viewItems():
        """Function that lists all items in the database to view"""
        cur.execute('SELECT * FROM inventory')
        rows = cur.fetchall()
        return rows

    def searchItem():
        """Function that allows users to search for a specific itme"""
        itemName = input('Enter name of the item you want to search:')
        cur.execute('SELECT itemName FROM inventory WHERE itemName=?', (itemName,))
        exists = cur.fetchone()
        if exists:
            cur.execute("SELECT * FROM inventory WHERE itemName=?", (itemName,))
            rows = cur.fetchall()
            return rows
        else:
            print("Item does not exist.")
            exit()