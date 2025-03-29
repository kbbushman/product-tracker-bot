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


def get_products():
    conn = create_connection()
    products = []
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, url, threshold, date_added FROM products;")

            # Fetch all rows and convert them into dictionaries
            rows = cursor.fetchall()

            for row in rows:
                product = {
                    "id": row[0],
                    "name": row[1],
                    "url": row[2],
                    "threshold": row[3],
                    "date_added": row[4],
                }
                products.append(product)
        except Error as e:
            print(f"Error fetching products: {e}")
        finally:
            conn.close()

    return products
