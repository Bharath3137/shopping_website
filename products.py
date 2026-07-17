class ProductManager:

    def __init__(self, databasemanager):
        self.databasemanager = databasemanager

    def get_all_products(self):
        query = "SELECT * FROM products"
        return self.databasemanager.execute_query(query)

    def get_product(self, product_id):
        query = f"SELECT * FROM products WHERE id={product_id}"
        products = self.databasemanager.execute_query(query)

        if products:
            return products[0]
        return None

    def is_valid_product(self, product_id):
        return self.get_product(product_id) is not None

    def search_product(self, name):
        query = f"SELECT * FROM products WHERE name='{name}'"
        return self.databasemanager.execute_query(query)

    def add_product(self, name, price, stock, category):

        query = f"""
        INSERT INTO products(name, price, stock, category)
        VALUES('{name}', {price}, {stock}, '{category}')
        """

        self.databasemanager.execute_query(query)

        return "Product Added Successfully"

    def update_product(self, product_id, field, value):

        if not self.is_valid_product(product_id):
            return "Product Not Found"

        if isinstance(value, str):
            value = f"'{value}'"

        query = f"""
        UPDATE products
        SET {field}={value}
        WHERE id={product_id}
        """

        self.databasemanager.execute_query(query)

        return "Product Updated Successfully"

    def delete_product(self, product_id):

        if not self.is_valid_product(product_id):
            return "Product Not Found"

        query = f"DELETE FROM products WHERE id={product_id}"

        self.databasemanager.execute_query(query)

        return "Product Deleted Successfully"