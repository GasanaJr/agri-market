import sqlite3


def buyerViewSeller():
    # CREATE VARIABLES
    conn = sqlite3.connect('e-comm.db')
    cur = conn.cursor()
    buyer = int(input("Enter your buyer's Id "))
    cur.execute('''
    SELECT sellers.name, sellers.telephone, products.name FROM products join sellers ON sellers.id = products.seller_id WHERE products.buyer_id == ?
    ''', (buyer,))
    rows = cur.fetchall()
    if len(rows) <= 0:
        print("*********** You don't have any orders ************")
    print("All Oders Info Available On Your Account")
    print("************************************************************")
    for row in rows:
        print(f'''
        Seller's Name:          {row[0]} 
        Seller's Phone number:  {row[1]}
        Product's Name:         {row[2]}
        ''')
