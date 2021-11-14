import sqlite3

name = 'base.db'
db = sqlite3.connect(name)

cur = db.cursor()
products = ('''
CREATE TABLE "Products" (
product_id INTEGER PRIMARY KEY, image BLOB, product_name TEXT, cost REAL, structure TEXT, exp_date TEXT, description TEXT
)''')
cur.execute(products)

clients = ('''
CREATE TABLE Clients(
client_id TEXT, name TEXT, surname TEXT, mail TEXT, phone TEXT
)''')
cur.execute(clients)

orders = ('''
CREATE TABLE "Orders" (
order_id INTEGER PRIMARY KEY, client_id TEXT, items_id TEXT, shipping_address TEXT, shipping date TEXT, cost REAL, FOREIGN KEY (client_id) REFERENCES Clients(client_id)
)''')
cur.execute(orders)

db.commit()
