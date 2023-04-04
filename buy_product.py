import sqlite3


def buy_product():
    # CREATE VARIABLES
    conn = sqlite3.connect('e-comm.db')
    cur = conn.cursor()

    product = int(input("Enter the Product's Id "))
    user = int(input("Enter your Buyer's Id "))

    cur.execute('''
    UPDATE products SET buyer_id = ? WHERE id= ?
    ''', (user, product,))

    print("Order Placed Successfully! The seller will be in Touch Shortly")
    print("****************************************************************")

    conn.commit()
