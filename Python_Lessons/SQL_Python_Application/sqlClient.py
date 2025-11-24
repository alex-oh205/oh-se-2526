"""
Name: Alex Oh
Date: 11/19/25

File: sqlClient.py

Purpose: Client interface for SQLite database
"""

import sqlite3, sqlLib
from sqlite3 import Error

#-----------------------  Format OrderItems Result Set  ------------------------
def OIresult(rows):
    print("{0:^14} {1:^14} {2:^15} {3:^13}".format
    ("Product ID", "Quantity", "Item Price ($)", "Taxed Price ($)")) # Print the data in a table

    print("{0:14} {1:14} {2:15} {3:13}".format("-"*14, "-"*14, "-"*15, "-"*13))

    for row in rows:
        prodID = row[0]
        quant = int(row[1])
        itemPrice = float(row[2])
        taxPrice = float(row[3])

        print("{0:^14} {1:^14} {2:^15.2f} {3:^13.2f}".format
        (prodID, quant, itemPrice, taxPrice))   # Print the data in a table

#---------------------  Gather Inputs for Product Insert  ----------------------
def prodInsertInputs():
    """ Gather product input data
        Args:
            None
        Returns:
            list of the corresponding product data (pid, vendor, name, price,
            desc)
    """

    p = []  # Use a list to store the product information

    print("Please enter the following information:")
    pid = input("Enter the product ID: ")
    p.append(pid)

    vendor = input("Enter the vendor ID (BRS01, BRS02, DLL01, FRB01, JTS01): ")

    p.append(vendor)

    name = input("Enter the product name (255 characters max): ")
    p.append(name)

    price = float(input("Enter the product price:  $"))
    p.append(price)

    desc = input("Enter the product description: ")
    p.append(desc)

    return p    # Return the product information for SQL INSERT

#------------------------  Format Product Result Set  --------------------------
def prodResult(rows):
    print("{0:^13} {1:^13} {2:^20} {3:^15} {4:^46}".format
    ("Product ID", "Vendor ID", "Name", "Price ($)", "Description")) # Print the data in a table

    print("{0:13} {1:13} {2:20} {3:15} {4:46}".format
    ("-"*13, "-"*13, "-"*20, "-"*15, "-"*46))

    for row in rows:
        prodID = row[0]
        vendID = row[1]
        name = row[2]
        price = float(row[3])
        desc = row[4]

        print("{0:^13} {1:^13} {2:^20} {3:^16.2f} {4:<40}".format
        (prodID, vendID, name, price, desc))   # Print the data in a table

#---------------------  Gather Inputs for Vendor Insert  -----------------------
def vendInsertInputs():
    """ Gather vendor input data
        Args:
            None
        Returns:
            list of the corresponding vendor data (vid, name, address, city,
             state, zip, country)
    """

    v = []  # Use a list to store the vendor information

    print("Please enter the following information:")
    vid = input("Enter the vendor ID: ")
    v.append(vid)

    name = input("Enter the vendor name: ")
    v.append(name)

    address = input("Enter the vendor address: ")
    v.append(address)

    city = input("Enter the vendor city: ")
    v.append(city)

    state = input("Enter the vendor state: ")
    v.append(state)

    zip = input("Enter the vendor zip: ")
    v.append(zip)

    country = input("Enter the vendor country: ")
    v.append(country)

    return v    # Return the vendor information for SQL INSERT

#------------------------  Format Vendor Result Set  ---------------------------
def vendResult(row):
    print("{0:^24} {1:^20} {2:^13} {3:^13}".format
    ("Name", "Address", "City", "State")) # Print the data in a table

    print("{0:^24} {1:^20} {2:^13} {3:^13}".format
    ("-"*24, "-"*20, "-"*13, "-"*13))

    name = row[0]
    address = row[1]
    city = row[2]
    state = row[3]

    print("{0:^24} {1:^20} {2:^13} {3:^13}".format
    (name, address, city, state))   # Print the data in a table

#---------------------  Gather Inputs for Customer Update  ---------------------
def custUpdateInputs():
    """ Gather customer input data
        Args:
            None
        Returns:
            list of the corresponding customer data (cid, [contact, email])
    """

    c = []  # Use a list to store the customer information

    print("Please enter the following information:")
    cid = input("Enter the customer ID: ")
    c.append(cid)

    contact = input("Enter the customer contact: ")
    email = input("Enter the customer email: ")
    c.append([contact, email])

    return c    # Return the customer information for SQL UPDATE

#------------------------  Format Customer Result Set  -------------------------
def custResult(row):
    print("{0:^13} {1:^20}".format
    ("Name", "Email")) # Print the data in a table

    print("{0:13} {1:20}".format
    ("-"*13, "-"*20))

    name = row[0]
    email = row[1]

    print("{0:^13} {1:^20}".format
    (name, email))   # Print the data in a table

#------------------------  main() for script testing  --------------------------
def main():
    database = "tysql_copy.sqlite"              # SQLite database to use

    conn = sqlLib.create_connection(database)   # Create a database connection

#-----------------------  Test SELECT on OrderItems  ---------------------------
    # result = sqlLib.select_orderItems(conn)     # Query OrderItems
    # OIresult(result)                           # Format result

#-----------------------  Test INSERT Product  ---------------------------------
    # product = prodInsertInputs()                    # Gather product information
    # rowID = sqlLib.insert_product(conn, product)    # Insert a new product row
    #                                                 # in table Products
    # print(rowID)

#-----------------------  Test SELECT Product  ---------------------------------
    products = sqlLib.select_products(conn)         # Query Products
    prodResult(products)                            # format result

#-----------------------  Test INSERT Vendor  ----------------------------------
    # vendor = vendInsertInputs()                   # Gather vendor information
    # rowID = sqlLib.insert_vendor(conn, vendor)    # Insert a new vendor row
    #                                               # in table Vendors
    # print(rowID)

#-----------------------  Test SELECT Vendor  ----------------------------------
    # vendorID = "OMS01"
    # vendor = sqlLib.select_vendor(conn, vendorID)     # Query Vendors
    # vendResult(vendor)                                # format result

#-----------------------  Test INSERT Vendor  ----------------------------------
    # custUpdate = custUpdateInputs()                                       # Gather customer update info
    # rowID = sqlLib.update_customer(conn, custUpdate[0], custUpdate[1])    # Update customer info
    #                                                                       # in table Customers
    # print(rowID)

#-----------------------  Test SELECT Customer  --------------------------------
    # custID = "1000000005"
    # customer = sqlLib.select_customer(conn, custID)       # Query Customers
    # custResult(customer)                                  # format result

if __name__ == "__main__":
    main()