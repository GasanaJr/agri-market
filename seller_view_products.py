import sqlite3
import seller_view_orders


def sellerViewProduct():

    # CREATE VARIABLES
    conn = sqlite3.connect('e-comm.db')
    cur = conn.cursor()
    seller_id = int(input("Enter your Seller Id "))

    cur.execute('''
    SELECT * FROM products WHERE seller_id = ?
    ''', (seller_id,))
    rows = cur.fetchall()
    if len(rows) <= 0:
        print("*********** You don't have any products ************")
    else:
        while True:
            print("Your Products")
            print("************************************************************")
            for row in rows:
                print(f'''
                Product Id:          {row[0]} 
                Product Name:        {row[1]}
                Product Quantity:    {row[2]}
                Product Price:       {row[3]}
                Product Description: {row[4]}
                ''')
            seller_choice = int(input('''
            Enter 1 to see orders
            Enter 0 to Quit
            '''))
            if (seller_choice == 1):
                seller_view_orders.sellerViewOrders()
            else:
                break
