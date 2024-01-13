import sqlite3

class ShopDB:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("shop.db")
        self.cursor = self.conn.cursor()

    def total_sales(self):
        self.cursor.execute('''SELECT SUM(p.price * o.quantity) AS total_sales
                            FROM orders o
                            INNER JOIN products p ON o.product_id = p.product_id;''')
        data = self.cursor.fetchall()
        return data

    def close(self):
        self.conn.close()