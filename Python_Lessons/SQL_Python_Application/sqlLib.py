"""
Name: Alex Oh
Date: 11/19/25

File: sqlLib.py

Purpose: Library of functions for SQLite tutorial
"""

import sqlite3
from sqlite3 import Error

def create_connection(db):
    """ Create a connection to the SQLite database
        Args:
            param1: db - the database file
        Returns:
            connection object or None if unable to connect
    """

    try:
        conn = sqlite3.connect(db)
        print("Database connection established.")
        return conn
    except Error as e:
        print(e)
    
    return None

def select_orderItems(conn):
    """ Query: prod_id, quantity, item_price, calculated tax price from
        OrderItems

        Args:
            param1: conn - the connection object
        Returns:
            the queried data
    """
    cur = conn.cursor() # Create cursor to store the result set to
                        # Allows you to move forward or backward through the
                        # results set row by row
    cur.execute('''SELECT prod_id, quantity, item_price, quantity * item_price
                   * 1.07 AS 'taxed_price(7%)' FROM OrderItems WHERE order_num =
                   20006;''')

    rows = cur.fetchall()   # Fetches all (or remaining) rows of query result
                            # and returns a list of tuples
    cur.close()
    return rows

def insert_product(conn, product):
    """ Add a product to the Products table
        Args:
            param1: conn - connection object for SQL database
            param2: product - a list containing the prod. info. for 
                              insertion into table products
        Returns:
            rowID of last successful insert
    """
    sql = '''INSERT INTO Products(prod_id, vend_id, prod_name, prod_price,
             prod_desc) VALUES(?,?,?,?,?);'''
    cur = conn.cursor()
    cur.execute(sql, product)
    conn.commit()               # Commit table updates to finalize them
    cur.close()
    return cur.lastrowid

def select_products(conn):
    """ Query: prod_id, vendor, name, price, description FROM Products
        Args:
            param1: conn - the connection object
        Returns:
            the queried data
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Products;")

    rows = cur.fetchall()   # Fetches all (or remaining) rows of query result
                            # and returns a list of tuples
    cur.close()
    return rows

def insert_vendor(conn, vendor):
    """ Add a product to the Products table
        Args:
            param1: conn - connection object for SQL database
            param2: vendor - a list containing the vend. info. for 
                              insertion into table vendors
        Returns:
            rowID of last successful insert
    """
    sql = '''INSERT INTO Vendors(vend_id, vend_name, vend_address, vend_city,
             vend_state, vend_zip, vend_country) VALUES(?,?,?,?,?,?,?);'''
    cur = conn.cursor()
    cur.execute(sql, vendor)
    conn.commit()               # Commit table updates to finalize them
    cur.close()
    return cur.lastrowid

def select_vendor(conn, vendorID):
    """ Query: vend_name, vend_address, vend_city, vend_state FROM Vendors
        Args:
            param1: conn - the connection object
            param2: vendorID - the vendor ID to select
        Returns:
            the queried data
    """
    cur = conn.cursor()
    cur.execute('''SELECT vend_name, vend_address, vend_city, vend_state FROM Vendors
                   WHERE vend_id = ?;''', [vendorID])

    row = cur.fetchone()   # Fetches one row of query result
    cur.close()
    return row

def update_customer(conn, custID, contactInfo):
    """ Add a product to the Products table
        Args:
            param1: conn - connection object for SQL database
            param2: custID - the customer ID to update
            param3: contactInfo - a list containing the new customer name
                                  and email address
        Returns:
            rowID of last successful update
    """
    sql = '''UPDATE Customers SET cust_contact = ?, cust_email = ?
             WHERE cust_id = ?;'''
    cur = conn.cursor()
    cur.execute(sql, [contactInfo[0], contactInfo[1], custID])
    conn.commit()               # Commit table updates to finalize them
    cur.close()
    return cur.lastrowid

def select_customer(conn, customer):
    """ Query: cust_name, cust_email FROM Customers
        Args:
            param1: conn - the connection object
            param2: customer - the customer ID to select
        Returns:
            the queried data
    """
    cur = conn.cursor()
    cur.execute('''SELECT cust_name, cust_email FROM Customers
                   WHERE cust_id = ?;''', [customer])

    row = cur.fetchone()   # Fetches one row of query result
    cur.close()
    return row