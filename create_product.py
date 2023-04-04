import sqlite3

# CREATE VARIABLES
conn = sqlite3.connect('e-comm.db')
cur = conn.cursor()


def create_product():
    name = input("Enter name of the product ")
    quantity = int(input("Enter the quantity of the product "))
    price = float(input("Enter the unit price of the products "))
    desc = input("Provide a description of your product ")
    seller = input("Enter your seller ID ")

    cur.execute('''
    INSERT INTO products VALUES (?,?,?,?,?,?,?)
    ''', (None, name, quantity, price, desc, seller, None,))

    print("************** Product Created Successfully ***********************")

    conn.commit()
