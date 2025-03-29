import sqlite3
from sqlite3 import Error


# Initialize and connect to the database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("product_tracker.db")
        return conn
    except Error as e:
        print(e)
    return conn


# Create a table for products
def create_table():
    conn = create_connection()
    if conn:
        try:
            create_products_table = """
              CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                url TEXT NOT NULL,
                threshold REAL,
                date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
              );
            """
            cursor = conn.cursor()
            cursor.execute(create_products_table)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()


# Add a product to the database
def add_product(name, url, threshold):
    conn = create_connection()
    if conn:
        try:
            sql_insert_product = """
              INSERT INTO products (name, url, threshold)
              values (?, ?, ?);
            """
            cursor = conn.cursor()
            cursor.execute(sql_insert_product, (name, url, threshold))
            conn.commit()
        except Error as e:
            print(f"Error adding product: {e}")
        finally:
            conn.close()
