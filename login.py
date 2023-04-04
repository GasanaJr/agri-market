import sqlite3
import create_product
import view_product
import seller_view_products


def login():
    # CREATE VARIABLES
    conn = sqlite3.connect('e-comm.db')
    cur = conn.cursor()

    # GET USER DATA
    while True:
        print("Log into your account to continue")
        print("**************************************************************")
        email = input("Enter your Email ")
        password = input("Enter your Password ")
        role = int(input('''
                Enter your proffession 
                1. Seller
                2. Buyer
                0. Quit
            '''))

        if (role == 1):
            cur.execute('SELECT * FROM sellers WHERE email = ?', (email,))
            row = cur.fetchone()
            if row is None:
                print("Email is invalid! Please Sign Up")
            elif password != row[4]:
                print("Incorrect Password! Please try again")
            else:
                print(f"Welcome {row[1]} your id is {row[0]} ")
                print("***************************************************")
                while True:
                    seller_choice = int(input('''
                Enter 1 to view products and orders
                Enter 2 to create product
                Enter 0 to Quit
                '''))
                    if (seller_choice == 1):
                        seller_view_products.sellerViewProduct()
                    elif (seller_choice == 0):
                        break
                    else:
                        create_product.create_product()

        elif (role == 2):
            cur.execute('SELECT * FROM buyers WHERE email = ?', (email,))
            row = cur.fetchone()
            if row is None:
                print("Email is invalid! Please Sign Up")
            elif password != row[4]:
                print("Incorrect Password! Please try again")
            else:
                print(f"Welcome {row[1]} your id is {row[0]} ")
                print("***************************************************")
                view_product.view_product()
        elif (role == 0):
            break

    cur.close()
