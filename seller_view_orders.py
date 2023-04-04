import sqlite3


def sellerViewOrders():
    # CREATE VARIABLES
    conn = sqlite3.connect('e-comm.db')
    cur = conn.cursor()

    product = int(input("Enter the Product Id to View orders "))

    cur.execute('''
    SELECT buyers.name, buyers.telephone, products.name 
    FROM products join buyers ON buyers.id == products.buyer_id
    WHERE products.id = ?
    ''', (product,))
    rows = cur.fetchall()
    if len(rows) <= 0:
        print("*********** You don't have any orders ************")
    else:
        print("All Oders Available for the Selected Product")
        print("************************************************************")
        for row in rows:
            print(f'''
            Buyer's Name:          {row[0]} 
            Buyer's Phone number:  {row[1]}
            Product's Name:        {row[2]}
            ''')
