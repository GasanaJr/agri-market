import sqlite3
import buy_product
import buyer_view_seller


def view_product():

    # CREATE VARIABLES
    conn = sqlite3.connect('e-comm.db')
    cur = conn.cursor()

    cur.execute('''
    SELECT * FROM products
    ''')
    rows = cur.fetchall()
    while True:
        print("All Products Available at the Market Place")
        print("************************************************************")
        for row in rows:
            print(f'''
            Product Id:          {row[0]} 
            Product Name:        {row[1]}
            Product Quantity:    {row[2]}
            Product Price:       {row[3]}
            Product Description: {row[4]}
            ''')
        buyer_choice = int(input('''
        Enter 1 to buy
        Enter 2 to see orders
        Enter 0 to Quit
        '''))
        if (buyer_choice == 1):
            buy_product.buy_product()
        elif (buyer_choice == 0):
            break
        else:
            buyer_view_seller.buyerViewSeller()
