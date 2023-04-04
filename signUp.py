import sqlite3
import login


def signUp():
    # CREATE VARIABLES
    conn = sqlite3.connect('e-comm.db')
    cur = conn.cursor()

    # TABLE CREATION
    try:
        cur.execute('''
                CREATE TABLE sellers (
                id INTEGER PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                telephone VARCHAR(20),
                password VARCHAR(255)
                )
                ''')
        cur.execute('''
                CREATE TABLE buyers(
                id INTEGER PRIMARY KEY,
                name VARCHAR(25),
                email VARCHAR(25),
                telephone VARCHAR(25),
                password VARCHAR(255)
                )
                ''')
        cur.execute('''
                CREATE TABLE products(
                id INTEGER PRIMARY KEY,
                name VARCHAR(255),
                quantity INTEGER,
                price REAL,
                description VARCHAR(1000),
                seller_id INTEGER,
                buyer_id INTEGER,
                FOREIGN KEY(seller_id) REFERENCES seller(id),
                FOREIGN KEY(buyer_id) REFERENCES buyer(id)
                )
                ''')

    except:
        pass

    # GET USER DATA
    print("Sign up for the Market Place")
    print("**************************************************************")

    name = input("Enter your Name ")
    email = input("Enter your Email ")
    password = input("Enter your Password ")
    telephone = input("Enter your telephone number")
    profession = int(input('''
        Enter your proffession 
        1. Seller
        2. Buyer
    '''))

    # INSERT DATA TO OUR DATABASE

    if (profession == 1):
        cur.execute(''' 
    INSERT INTO sellers VALUES(?,?,?,?,?)
    ''', (None, name, email, telephone, password,))
    elif (profession == 2):
        cur.execute(''' 
    INSERT INTO buyers VALUES(?,?,?,?,?)
    ''', (None, name, email, telephone, password,))

    conn.commit()

    print("Proceeding to Login .......")
    print("*******************************")
    login.login()
