import sqlite3

def connect_db():
    return sqlite3.connect("inventory.db")

def setup_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            stock_quantity INTEGER,
            price REAL,
            low_stock_alert INTEGER
        )
    """)
    conn.commit()
    conn.close()

def fetch_all_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

def add_product(name, category, stock_quantity, price, low_stock_alert):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products (name, category, stock_quantity, price, low_stock_alert)
        VALUES (?, ?, ?, ?, ?)
    """, (name, category, stock_quantity, price, low_stock_alert))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()
